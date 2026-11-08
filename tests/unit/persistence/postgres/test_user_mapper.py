# # tests/unit/persistence/postgres/mapper/test_user_mapper.py

# import pytest


# import pytest

# from src.gitrec.domain.entity.user.user_item import UserItem
# from src.gitrec.persistence.postgres.mapper.user import UserMapper


# @pytest.fixture
# def mapper() -> UserMapper:
#     return UserMapper()


# @pytest.fixture
# def sample_user() -> UserItem:
#     return UserItem(
#         id=123,
#         node_id="MDQ6VXNlcjEyMw==",
#         login="test_user",
#         avatar_url="https://example.com/avatar.png",
#         html_url="https://github.com/test_user",
#         type="User",
#         site_admin=False,
#     )


# def test_flatten_empty_users_returns_empty_records(mapper):
#     records = mapper.flatten([])

#     expected_keys = {
#         "users",
#         "events",
#         "followers",
#         "following",
#         "gists",
#         "organizations",
#         "profiles",
#         "received_events",
#         "starred",
#         "user_repositories",
#     }

#     assert set(records.keys()) == expected_keys

#     for resource_records in records.values():
#         assert resource_records == []


# def test_flatten_rejects_non_list_input(mapper):
#     with pytest.raises(TypeError):
#         mapper.flatten("invalid")


# def test_flatten_rejects_invalid_user_instance(mapper):
#     with pytest.raises(TypeError):
#         mapper.flatten(["invalid"])


# def test_map_user_returns_correct_record(mapper, sample_user):
#     record = mapper._map_user(sample_user)

#     assert record == {
#         "id": 123,
#         "node_id": "MDQ6VXNlcjEyMw==",
#         "login": "test_user",
#         "avatar_url": "https://example.com/avatar.png",
#         "html_url": "https://github.com/test_user",
#         "type": "User",
#         "site_admin": False,
#     }


# def test_map_profile_returns_empty_list_when_profile_missing(
#     mapper,
#     sample_user,
# ):
#     records = mapper._map_profile(sample_user)

#     assert records == []


# def test_flatten_maps_user_with_no_nested_resources(
#     mapper,
#     sample_user,
# ):
#     records = mapper.flatten([sample_user])

#     assert records["users"] == [
#         mapper._map_user(sample_user)
#     ]

#     assert records["profiles"] == []
#     assert records["events"] == []
#     assert records["followers"] == []
#     assert records["following"] == []
#     assert records["gists"] == []
#     assert records["organizations"] == []
#     assert records["received_events"] == []
#     assert records["starred"] == []
#     assert records["user_repositories"] == []





# from src.gitrec.domain.entity.user.event_item import EventItem


# @pytest.fixture
# def sample_event() -> EventItem:
#     return EventItem(
#         id="123456",
#         type="PushEvent",
#         actor_id=100,
#         actor_login="test_user",
#         repo_id=200,
#         repo_name="test_user/test_repo",
#         payload={"action": "push"},
#         created_at="2026-01-15T10:30:00Z",
#     )


#     def test_map_events_returns_correct_records(mapper, sample_user, sample_event):
#     sample_user.events.append(sample_event)

#     records = mapper._map_events(sample_user)

#     assert records == [
#         {
#             "id": "123456",
#             "type": "PushEvent",
#             "actor_id": 100,
#             "actor_login": "test_user",
#             "repo_id": 200,
#             "repo_name": "test_user/test_repo",
#             "payload": {"action": "push"},
#             "created_at": "2026-01-15T10:30:00Z",
#         }
#     ]


#     def test_map_events_returns_empty_list_when_no_events(
#     mapper,
#     sample_user,
# ):
#     records = mapper._map_events(sample_user)

#     assert records == []

#     def test_map_events_maps_multiple_events(
#     mapper,
#     sample_user,
#     sample_event,
# ):
#     second_event = EventItem(
#         id="789012",
#         type="IssuesEvent",
#         actor_id=101,
#         actor_login="another_user",
#         repo_id=201,
#         repo_name="another_user/another_repo",
#         payload={"action": "opened"},
#         created_at="2026-01-16T10:30:00Z",
#     )

#     sample_user.events.extend([sample_event, second_event])

#     records = mapper._map_events(sample_user)

#     assert len(records) == 2
#     assert records[0]["id"] == "123456"
#     assert records[1]["id"] == "789012"