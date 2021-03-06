from enum import Enum
from dataclasses import dataclass, field

import misli

from misli import Entity
from misli.basic_classes import Point, Rectangle
from pamet.constants import RESIZE_CIRCLE_RADIUS

from misli_gui.base_view import View
from pamet_desktop.helpers import control_is_pressed, shift_is_pressed
from pamet.constants import MOVE_SPEED, MIN_HEIGHT_SCALE, MAX_HEIGHT_SCALE
from pamet.constants import INITIAL_EYE_Z
from pamet.entities import Note, Page

from pamet.note_components import usecases as notes_usecases
from pamet.map_page import usecases
from pamet.map_page.viewport import Viewport

log = misli.get_logger(__name__)


class MapPageMode(Enum):
    NONE = 0
    DRAG_NAVIGATION = 1
    DRAG_SELECT = 2
    NOTE_RESIZE = 3
    NOTE_DRAG = 4


@dataclass
class MapPageViewModel(Entity):
    page: Page = None

    geometry: Rectangle = Rectangle(0, 0, 500, 500)
    viewport_center: Point = Point(0, 0)
    viewport_height: float = INITIAL_EYE_Z

    selected_nc_ids: set = field(default_factory=set)

    drag_navigation_active: bool = False
    drag_navigation_start_position: Point = None

    drag_select_active: bool = False
    mouse_position_on_drag_select_start: Point = None
    drag_selected_nc_ids: list = field(default_factory=list)
    drag_select_rect_props: list = field(default_factory=list)

    note_resize_active: bool = False
    mouse_position_on_note_drag_start: Point = None
    note_resize_click_position: Point = None
    note_resize_delta_from_note_edge: Point = None
    note_resize_main_note: Note = None
    viewport_position_on_press: Point = None

    note_drag_active: bool = False

    def __post_init__(self):
        self.modes = MapPageMode
        self.viewport = Viewport(self)

    def mode(self):
        modes_sum = (self.drag_navigation_active +
                     self.drag_select_active +
                     self.note_resize_active +
                     self.note_drag_active)

        if not modes_sum:
            return self.modes.NONE

        elif modes_sum > 1:
            raise Exception('More than one mode activated')

        if self.drag_navigation_active:
            return self.modes.DRAG_NAVIGATION

        elif self.drag_select_active:
            return self.modes.DRAG_SELECT

        elif self.note_resize_active:
            return self.modes.NOTE_RESIZE

        elif self.note_drag_active:
            return self.modes.NOTE_DRAG


class MapPageView(View):
    view_class = 'MapPage'

    def __init__(self, parent_id: str):
        default_state = MapPageViewModel(
            page=Page(),
            selected_nc_ids=set(),
            viewport_position_on_press=Point(0, 0),
            drag_navigation_active=False,
            drag_select_active=False,
            drag_selected_nc_ids=[],
            drag_select_rect_props=[],
            note_resize_active=False,
            note_resize_click_position=Point(0, 0),
            note_resize_delta_from_note_edge=Point(0, 0)
        )

        View.__init__(
            self,
            parent_id,
            initial_model=default_state)

        self._left_mouse_is_pressed = False
        self._mouse_position_on_left_press = Point(0, 0)

    @property
    def page(self):
        return self.last_model.page.copy()

    @property
    def viewport(self):
        return self.last_model.viewport

    # def set_state_from_page(self, page):
    #     self._page = page

    def get_note_views_in_area(self, rect: Rectangle):
        unprojected_rect = self.viewport.unproject_rect(rect)
        intersecting = []

        for child in self.get_children():
            if child.note.rect().intersects(unprojected_rect):
                intersecting.append(child)

        return intersecting

    def get_note_views_at(self, position: Point):
        unprojected_mouse_pos = self.viewport.unproject_point(position)
        intersecting = []

        for child in self.get_children():
            note = child.note

            if note.rect().contains(unprojected_mouse_pos):
                intersecting.append(child)

        return intersecting

    def get_note_view_at(self, position: Point):
        intersecting = self.get_note_views_at(position)
        if not intersecting:
            return None

        return intersecting[0]

    def resize_circle_intersect(self, position: Point):
        state = self.last_model
        for nc in self.get_children():
            if nc.id not in state.selected_nc_ids:
                continue

            unprojected_pos = self.viewport.unproject_point(position)
            resize_circle_center = nc.note.rect().bottom_right()

            distance = resize_circle_center.distance_to(unprojected_pos)
            if distance <= RESIZE_CIRCLE_RADIUS:
                return nc

    def handle_delete_shortcut(self):
        usecases.delete_selected_notes(self.id)

    def handle_left_mouse_long_press(self, mouse_pos: Point):
        if self.last_model.note_resize_active:
            return

        ncs_under_mouse = self.get_note_views_at(mouse_pos)
        if ncs_under_mouse:
            usecases.start_note_drag(self.id, mouse_pos.to_list())

    def handle_left_mouse_press(self, mouse_pos: Point):
        self._mouse_position_on_left_press = mouse_pos
        self._left_mouse_is_pressed = True

        ctrl_pressed = control_is_pressed()
        shift_pressed = shift_is_pressed()

        nc_under_mouse = None
        ncs_under_mouse = self.get_note_views_at(mouse_pos)
        if ncs_under_mouse:
            nc_under_mouse = ncs_under_mouse[0]

        resize_nc = self.resize_circle_intersect(mouse_pos)

        if ctrl_pressed and shift_pressed:
            usecases.start_drag_select(self.id, mouse_pos.to_list())
            return

        if ctrl_pressed:
            if nc_under_mouse:
                nc_selected = nc_under_mouse.id in self.last_model.selected_nc_ids
                usecases.update_note_selections(
                    self.id, {nc_under_mouse.id: not nc_selected})

        # Clear selection (or reduce it to the note under the mouse)
        if not ctrl_pressed and not shift_pressed:
            if resize_nc:
                nc_under_mouse = resize_nc

            usecases.clear_note_selection(self.id)

            if nc_under_mouse:
                usecases.update_note_selections(
                    self.id, {nc_under_mouse.id: True})

        # Check for resize initiation
        if resize_nc:
            if resize_nc.id not in self.last_model.selected_nc_ids:
                usecases.update_note_selections(self.id, {resize_nc.id: True})

            resize_circle_center = resize_nc.note.rect().bottom_right()
            rcc_projected = self.viewport.project_point(resize_circle_center)
            usecases.start_notes_resize(
                self.id, resize_nc.note, mouse_pos, rcc_projected)

            return

    def handle_left_mouse_release(self, mouse_pos: Point):
        self._left_mouse_is_pressed = False

        state: MapPageViewModel = self.last_model
        mode = state.mode()

        if state.drag_select_active:
            usecases.stop_drag_select(self.id)

        elif state.note_resize_active:
            new_size = self._new_note_size_on_resize(mouse_pos)
            usecases.stop_notes_resize(
                self.id, new_size, state.selected_nc_ids)

        elif state.note_drag_active:
            pos_delta = mouse_pos - state.mouse_position_on_note_drag_start
            pos_delta /= self.viewport.height_scale_factor()
            usecases.stop_note_drag(
                self.id, state.selected_nc_ids, pos_delta.to_list())

        elif mode == state.modes.DRAG_NAVIGATION:
            usecases.stop_drag_navigation(self.id)

    def _new_note_size_on_resize(self, new_mouse_pos: Point):
        mouse_delta = new_mouse_pos - self.last_model.note_resize_click_position
        size_delta = mouse_delta - self.last_model.note_resize_delta_from_note_edge

        size_delta = size_delta / self.viewport.height_scale_factor()
        new_size = self.last_model.note_resize_main_note.size() + size_delta

        return new_size

    def _handle_move_on_drag_select(self, mouse_pos: Point):
        selection_rect = Rectangle.from_points(
                self.last_model.mouse_position_on_drag_select_start, mouse_pos)

        ncs_in_selection = self.get_note_views_in_area(selection_rect)
        drag_selected_nc_ids = [nc.id for nc in ncs_in_selection]

        usecases.update_drag_select(
            self.id, selection_rect.to_list(), drag_selected_nc_ids)

    def handle_mouse_move(self, mouse_pos: Point):
        state = self.last_model
        mode = state.mode()
        delta = self._mouse_position_on_left_press - mouse_pos

        if mode == state.modes.NONE:
            if self._left_mouse_is_pressed:
                usecases.start_mouse_drag_navigation(
                    self.id, self._mouse_position_on_left_press, delta)

        if mode == state.modes.DRAG_SELECT:
            self._handle_move_on_drag_select(mouse_pos)

        elif mode == state.modes.NOTE_RESIZE:
            new_size = self._new_note_size_on_resize(mouse_pos)
            usecases.resize_note_views(
                self.id, new_size.to_list(), state.selected_nc_ids)

        elif mode == state.modes.NOTE_DRAG:
            pos_delta = mouse_pos - self._mouse_position_on_left_press
            pos_delta /= self.viewport.height_scale_factor()
            usecases.note_drag_nc_position_update(
                self.id, state.selected_nc_ids, pos_delta.to_list())

        elif mode == state.modes.DRAG_NAVIGATION:
            # Page drag navigation was active
            usecases.mouse_drag_navigation_move(self.id, delta)

    def handle_mouse_scroll(self, steps: int):
        delta = MOVE_SPEED * steps
        current_height = self.last_model.viewport_height

        new_height = max(MIN_HEIGHT_SCALE,
                         min(current_height - delta, MAX_HEIGHT_SCALE))

        usecases.set_viewport_height(self.id, new_height)

    def handle_left_mouse_double_click(self, mouse_pos: Point):
        nc = self.get_note_view_at(mouse_pos)

        if nc:
            notes_usecases.start_editing_note(
                self.parent_id, nc.id, mouse_pos.to_list())
        else:
            pos = self.viewport.unproject_point(mouse_pos)

            page = self.page
            note = Note(page_id=page.id, view_class='Text', text='')
            note.x = pos.x()
            note.y = pos.y()

            notes_usecases.create_new_note(
                self.parent_id, mouse_pos.to_list(), note.asdict())

    def handle_resize_event(self, width, height):
        usecases.resize_page(self.id, width, height)
