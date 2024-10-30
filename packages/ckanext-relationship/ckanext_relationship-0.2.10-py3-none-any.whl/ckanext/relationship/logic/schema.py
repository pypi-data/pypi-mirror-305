from ckan.logic.schema import validator_args


@validator_args
def relation_create(not_empty, one_of):
    return {
        "subject_id": [
            not_empty,
        ],
        "object_id": [
            not_empty,
        ],
        "relation_type": [
            one_of(["related_to", "child_of", "parent_of"]),
        ],
    }


@validator_args
def relation_delete(not_empty, one_of, ignore_missing):
    return {
        "subject_id": [
            not_empty,
        ],
        "object_id": [
            not_empty,
        ],
        "relation_type": [
            ignore_missing,
            one_of(["related_to", "child_of", "parent_of"]),
        ],
    }


@validator_args
def relations_list(not_empty, one_of, ignore_missing):
    return {
        "subject_id": [
            not_empty,
        ],
        "object_entity": [
            ignore_missing,
            one_of(["package", "organization", "group"]),
        ],
        "object_type": [
            ignore_missing,
        ],
        "relation_type": [
            ignore_missing,
            one_of(["related_to", "child_of", "parent_of"]),
        ],
    }


@validator_args
def relations_ids_list(not_empty, one_of, ignore_missing):
    return {
        "subject_id": [
            not_empty,
        ],
        "object_entity": [
            ignore_missing,
            one_of(["package", "organization", "group"]),
        ],
        "object_type": [
            ignore_missing,
        ],
        "relation_type": [
            ignore_missing,
            one_of(["related_to", "child_of", "parent_of"]),
        ],
    }


@validator_args
def get_entity_list(not_empty, one_of):
    return {
        "entity": [
            not_empty,
            one_of(["package", "organization", "group"]),
        ],
        "entity_type": [
            not_empty,
        ],
    }


@validator_args
def autocomplete(not_empty):
    return {
        "incomplete": [],
        "current_entity_id": [
            not_empty,
        ],
        "entity_type": [
            not_empty,
        ],
        "updatable_only": [],
        "owned_only": [],
        "check_sysadmin": [],
        "format_autocomplete_helper": [],
    }
