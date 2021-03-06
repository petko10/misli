import misli
import misli_gui
import pamet

from misli.basic_classes import Point
from misli_gui.actions_lib import action

from pamet.entities import Note

log = misli.get_logger(__name__)


@action('map_page.start_mouse_drag_navigation')
def start_mouse_drag_navigation(
        map_page_view_id: str,
        mouse_position: Point,
        first_delta: Point):

    map_page_view_model = misli_gui.view_model(map_page_view_id)

    map_page_view_model.drag_navigation_active = True
    map_page_view_model.drag_navigation_start_position = mouse_position
    map_page_view_model.viewport_position_on_press = \
        map_page_view_model.viewport_center

    misli_gui.update_view_model(map_page_view_model)
    mouse_drag_navigation_move(map_page_view_id, first_delta)


def mouse_drag_navigation_move(map_page_view_id: str, mouse_delta: Point):
    map_page_view_model = misli_gui.view_model(map_page_view_id)

    unprojected_delta = (
        mouse_delta / map_page_view_model.viewport.height_scale_factor())
    new_viewport_center = (map_page_view_model.viewport_position_on_press
                           + unprojected_delta)

    change_viewport_center(
        map_page_view_id, new_viewport_center.to_list())


@action('map_page.change_viewport_center')
def change_viewport_center(
        map_page_view_id: str, new_viewport_center: Point):

    map_page_view_model = misli_gui.view_model(map_page_view_id)

    map_page_view_model.viewport_center = Point(*new_viewport_center)
    misli_gui.update_view_model(map_page_view_model)


@action('map_page.stop_drag_navigation')
def stop_drag_navigation(
        map_page_view_id: str):

    map_page_view_model = misli_gui.view_model(map_page_view_id)
    map_page_view_model.drag_navigation_active = False
    misli_gui.update_view_model(map_page_view_model)


@action('map_page.update_note_selections')
def update_note_selections(
        map_page_view_id: str, selection_updates_by_note_id: dict):

    map_page_view_model = misli_gui.view_model(map_page_view_id)

    if not selection_updates_by_note_id:
        return

    selection_update_count = 0

    for note_id, selected in selection_updates_by_note_id.items():

        if note_id in map_page_view_model.selected_nc_ids and not selected:
            map_page_view_model.selected_nc_ids.remove(note_id)
            selection_update_count += 1

        elif note_id not in map_page_view_model.selected_nc_ids and selected:
            map_page_view_model.selected_nc_ids.add(note_id)
            selection_update_count += 1

        else:
            log.warning('Redundant entry in selection_updates_by_note_id')

    if selection_update_count > 0:
        misli_gui.update_view_model(map_page_view_model)
        # log.info('Updated %s selections' % selection_update_count)
    else:
        log.info('No selections updated out of %s' %
                 selection_updates_by_note_id)


@action('map_page.clear_note_selection')
def clear_note_selection(map_page_view_id: str):
    map_page_view_model = misli_gui.view_model(map_page_view_id)

    selection_updates = {}
    for sc_id in map_page_view_model.selected_nc_ids:
        selection_updates[sc_id] = False

    if not selection_updates:
        return

    update_note_selections(map_page_view_id, selection_updates)


@action('map_page.set_viewport_height')
def set_viewport_height(map_page_view_id: str, new_height: float):
    map_page_view_model = misli_gui.view_model(map_page_view_id)
    map_page_view_model.viewport_height = new_height

    misli_gui.update_view_model(map_page_view_model)
    # //glutPostRedisplay(); artefact, thank you for siteseeing


@action('map_page.start_drag_select')
def start_drag_select(map_page_view_id: str, position: Point):
    map_page_view_model = misli_gui.view_model(map_page_view_id)

    map_page_view_model.mouse_position_on_drag_select_start = Point(*position)
    map_page_view_model.drag_select_active = True
    misli_gui.update_view_model(map_page_view_model)


@action('map_page.update_drag_select')
def update_drag_select(
        map_page_view_id: str,
        rect_props: list,
        drag_selected_nc_ids: list = None):

    map_page_view_model = misli_gui.view_model(map_page_view_id)

    if drag_selected_nc_ids is None:
        drag_selected_nc_ids = []

    map_page_view_model.drag_select_rect_props = rect_props
    map_page_view_model.drag_selected_nc_ids.clear()

    for nc_id in drag_selected_nc_ids:
        if nc_id not in map_page_view_model.drag_selected_nc_ids:
            map_page_view_model.drag_selected_nc_ids.append(nc_id)

    misli_gui.update_view_model(map_page_view_model)


@action('map_page.stop_drag_select')
def stop_drag_select(map_page_view_id: str):
    map_page_view_model = misli_gui.view_model(map_page_view_id)

    map_page_view_model.drag_select_active = False
    map_page_view_model.selected_nc_ids.update(
        map_page_view_model.drag_selected_nc_ids)
    map_page_view_model.drag_selected_nc_ids.clear()
    map_page_view_model.drag_select_rect_props = [0, 0, 0, 0]

    misli_gui.update_view_model(map_page_view_model)


@action('map_page.delete_selected_notes')
def delete_selected_notes(map_page_view_id: str):
    map_page_view_model = misli_gui.view_model(map_page_view_id)

    for nc_id in map_page_view_model.selected_nc_ids:
        ncs = misli_gui.view_model(nc_id)
        pamet.delete_note(ncs.note)


@action('map_page.start_notes_resize')
def start_notes_resize(
        map_page_view_id: str,
        main_note: Note,
        mouse_position: Point,
        resize_circle_center_projected: Point):

    map_page_view_model = misli_gui.view_model(map_page_view_id)

    map_page_view_model.note_resize_delta_from_note_edge = (
        resize_circle_center_projected - mouse_position)
    map_page_view_model.note_resize_click_position = mouse_position
    map_page_view_model.note_resize_main_note = main_note

    map_page_view_model.note_resize_active = True
    misli_gui.update_view_model(map_page_view_model)


@action('map_page.resize_note_views')
def resize_note_views(
        map_page_view_id: str, new_size: list, nc_ids: list):

    for nc_id in nc_ids:
        ncs = misli_gui.view_model(nc_id)
        note = ncs.note

        note.set_size(Point(*new_size))  # Here size restrictions are applied
        misli_gui.update_view_model(ncs)


@action('map_page.resize_notes')
def resize_notes(new_size: list, page_id: str, note_ids: list):
    for note_id in note_ids:
        note = pamet.note(page_id, note_id)

        note.set_size(new_size)
        pamet.update_note(note)


@action('map_page.stop_notes_resize')
def stop_notes_resize(
        map_page_view_id: str, new_size: list, nc_ids: list):

    map_page_view_model = misli_gui.view_model(map_page_view_id)
    map_page_view_model.note_resize_active = False

    page = map_page_view_model.page
    note_ids = [misli_gui.view(nc_id).note.id for nc_id in nc_ids]
    resize_notes(new_size, page.id, note_ids)

    misli_gui.update_view_model(map_page_view_model)


@action('map_page.start_note_drag')
def start_note_drag(
        map_page_view_id: str, mouse_pos: list):

    map_page_view_model = misli_gui.view_model(map_page_view_id)
    map_page_view_model.mouse_position_on_note_drag_start = Point(
        *mouse_pos)
    map_page_view_model.note_drag_active = True
    misli_gui.update_view_model(map_page_view_model)


# @action('map_page.note_drag_nc_position_update')
def note_drag_nc_position_update(
        map_page_view_id: str, nc_ids: list, delta: list):

    d = Point(*delta)

    for nc_id in nc_ids:
        ncs = misli_gui.view_model(nc_id)
        note = pamet.note(ncs.note.page_id, ncs.note.id)

        ncs.note.x = note.x + d.x()
        ncs.note.y = note.y + d.y()

        misli_gui.update_view_model(ncs)


@action('map_page.stop_note_drag')
def stop_note_drag(map_page_view_id: str, nc_ids: list, delta: list):
    map_page_view_model = misli_gui.view_model(map_page_view_id)

    d = Point(*delta)
    for nc_id in nc_ids:
        ncs = misli_gui.view_model(nc_id)
        note = pamet.note(ncs.note.page_id, ncs.note.id)

        note.x += d.x()
        note.y += d.y()

        pamet.update_note(note)

    map_page_view_model.note_drag_active = False
    misli_gui.update_view_model(map_page_view_model)


@action('map_page.select_all_notes')
def select_all_notes(map_page_view_id):
    map_page_view_model = misli_gui.view_model(map_page_view_id)

    for nc in misli_gui.view_children(map_page_view_id):
        map_page_view_model.selected_nc_ids.add(nc.id)

    misli_gui.update_view_model(map_page_view_model)


@action('map_page.resize_page')
def resize_page(map_page_view_id, width, height):
    map_page_view_model = misli_gui.view_model(map_page_view_id)
    map_page_view_model.geometry.set_size(width, height)
    misli_gui.update_view_model(map_page_view_model)
