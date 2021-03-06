from collections import defaultdict

import misli
import misli_gui
log = misli.get_logger(__name__)


class Binder:
    def __init__(self):
        self._view_ids_by_entity_id = defaultdict(list)
        self._entity_id_by_view_id = {}

    @log.traced
    def map_entity_to_view(self, entity, view):
        self._view_ids_by_entity_id[entity.gid()].append(view.id)
        self._entity_id_by_view_id[view.id] = entity.gid()

    @log.traced
    def unmap_entity_from_view(self, entity_gid, view_id):
        if view_id not in self._entity_id_by_view_id:
            raise Exception('Cannot unregister component that is not '
                            'registered ' % view_id)

        self._view_ids_by_entity_id[entity_gid].remove(view_id)
        del self._entity_id_by_view_id[view_id]

    @log.traced
    def views_mapped_to_entity(self, entity_gid):
        component_ids = self._view_ids_by_entity_id[entity_gid]
        components = []
        for component_id in component_ids:
            component = misli_gui.view(component_id)
            if not component:
                self.unmap_entity_from_view(entity_gid, component_id)
                continue

            components.append(component)

        return components

    # def entity_gid_for_component(self, component_id):
    #     if component_id not in self._entity_id_by_component_id:
    #         return None
    #
    #     return self._entity_id_by_component_id[component_id]

    # def handle_changes(self, changes):
    #     raise NotImplementedError
