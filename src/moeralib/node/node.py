# This file is generated

from typing import IO, Sequence, cast
from urllib.parse import quote_plus

from moeralib.node import schemas
from moeralib.node.caller import Caller
from moeralib.node import types
from moeralib.structure import comma_separated_flags, structure_list


class MoeraNode(Caller):

    def search_activity_reactions(self, filter: types.ActivityReactionFilter) -> Sequence[types.ActivityReactionInfo]:
        location = "/activity/reactions/search"
        data = self.call(
            "search_activity_reactions", location, method="GET", body=filter,
            schema=schemas.ACTIVITY_REACTION_INFO_ARRAY_SCHEMA
        )
        return structure_list(data, types.ActivityReactionInfo)

    def get_remote_posting_verification_status(self, id: str) -> types.RemotePostingVerificationInfo:
        location = "/async-operations/remote-posting-verification/{id}".format(id=quote_plus(id))
        data = self.call(
            "get_remote_posting_verification_status", location, method="GET",
            schema=schemas.REMOTE_POSTING_VERIFICATION_INFO_SCHEMA
        )
        return types.RemotePostingVerificationInfo(data)

    def get_remote_reaction_verification_status(self, id: str) -> types.RemoteReactionVerificationInfo:
        location = "/async-operations/remote-reaction-verification/{id}".format(id=quote_plus(id))
        data = self.call(
            "get_remote_reaction_verification_status", location, method="GET",
            schema=schemas.REMOTE_REACTION_VERIFICATION_INFO_SCHEMA
        )
        return types.RemoteReactionVerificationInfo(data)

    def get_avatars(self) -> Sequence[types.AvatarInfo]:
        location = "/avatars"
        data = self.call("get_avatars", location, method="GET", auth=False, schema=schemas.AVATAR_INFO_ARRAY_SCHEMA)
        return structure_list(data, types.AvatarInfo)

    def create_avatar(self, avatar: types.AvatarAttributes) -> types.AvatarInfo:
        location = "/avatars"
        data = self.call("create_avatar", location, method="POST", body=avatar, schema=schemas.AVATAR_INFO_SCHEMA)
        return types.AvatarInfo(data)

    def get_avatar(self, id: str) -> types.AvatarInfo:
        location = "/avatars/{id}".format(id=quote_plus(id))
        data = self.call("get_avatar", location, method="GET", auth=False, schema=schemas.AVATAR_INFO_SCHEMA)
        return types.AvatarInfo(data)

    def delete_avatar(self, id: str) -> types.Result:
        location = "/avatars/{id}".format(id=quote_plus(id))
        data = self.call("delete_avatar", location, method="DELETE", schema=schemas.RESULT_SCHEMA)
        return types.Result(data)

    def reorder_avatars(self, order: types.AvatarsOrdered) -> Sequence[types.AvatarOrdinal]:
        location = "/avatars/reorder"
        data = self.call(
            "reorder_avatars", location, method="POST", body=order, schema=schemas.AVATAR_ORDINAL_ARRAY_SCHEMA
        )
        return structure_list(data, types.AvatarOrdinal)

    def block_instant(self, instant: types.BlockedInstantAttributes) -> types.BlockedInstantInfo:
        location = "/blocked-instants"
        data = self.call(
            "block_instant", location, method="POST", body=instant, schema=schemas.BLOCKED_INSTANT_INFO_SCHEMA
        )
        return types.BlockedInstantInfo(data)

    def get_blocked_instant(self, id: str) -> types.BlockedInstantInfo:
        location = "/blocked-instants/{id}".format(id=quote_plus(id))
        data = self.call("get_blocked_instant", location, method="GET", schema=schemas.BLOCKED_INSTANT_INFO_SCHEMA)
        return types.BlockedInstantInfo(data)

    def unblock_instant(self, id: str) -> types.Result:
        location = "/blocked-instants/{id}".format(id=quote_plus(id))
        data = self.call("unblock_instant", location, method="DELETE", schema=schemas.RESULT_SCHEMA)
        return types.Result(data)

    def search_blocked_instants(self, filter: types.BlockedInstantFilter) -> Sequence[types.BlockedInstantInfo]:
        location = "/blocked-instants/search"
        data = self.call(
            "search_blocked_instants", location, method="POST", body=filter,
            schema=schemas.BLOCKED_INSTANT_INFO_ARRAY_SCHEMA
        )
        return structure_list(data, types.BlockedInstantInfo)

    def block_user(self, user: types.BlockedUserAttributes) -> types.BlockedUserInfo:
        location = "/people/blocked-users"
        data = self.call("block_user", location, method="POST", body=user, schema=schemas.BLOCKED_USER_INFO_SCHEMA)
        return types.BlockedUserInfo(data)

    def get_blocked_user(self, id: str) -> types.BlockedUserInfo:
        location = "/people/blocked-users/{id}".format(id=quote_plus(id))
        data = self.call("get_blocked_user", location, method="GET", schema=schemas.BLOCKED_USER_INFO_SCHEMA)
        return types.BlockedUserInfo(data)

    def unblock_user(self, id: str) -> types.Result:
        location = "/people/blocked-users/{id}".format(id=quote_plus(id))
        data = self.call("unblock_user", location, method="DELETE", schema=schemas.RESULT_SCHEMA)
        return types.Result(data)

    def search_blocked_users(self, filter: types.BlockedUserFilter) -> Sequence[types.BlockedUserInfo]:
        location = "/people/blocked-users/search"
        data = self.call(
            "search_blocked_users", location, method="POST", body=filter, schema=schemas.BLOCKED_USER_INFO_ARRAY_SCHEMA
        )
        return structure_list(data, types.BlockedUserInfo)

    def get_blocked_users_checksums(self) -> types.BlockedUsersChecksums:
        location = "/people/blocked-users/checksums"
        data = self.call(
            "get_blocked_users_checksums", location, method="GET", schema=schemas.BLOCKED_USERS_CHECKSUMS_SCHEMA
        )
        return types.BlockedUsersChecksums(data)

    def get_blocked_by_user(self, id: str) -> types.BlockedByUserInfo:
        location = "/people/blocked-by-users/{id}".format(id=quote_plus(id))
        data = self.call("get_blocked_by_user", location, method="GET", schema=schemas.BLOCKED_BY_USER_INFO_SCHEMA)
        return types.BlockedByUserInfo(data)

    def search_blocked_by_users(self, filter: types.BlockedByUserFilter) -> Sequence[types.BlockedByUserInfo]:
        location = "/people/blocked-by-users/search"
        data = self.call(
            "search_blocked_by_users", location, method="POST", body=filter,
            schema=schemas.BLOCKED_BY_USER_INFO_ARRAY_SCHEMA
        )
        return structure_list(data, types.BlockedByUserInfo)

    def get_cartes(self, limit: int | None = None) -> types.CarteSet:
        location = "/cartes".format()
        params = {"limit": limit}
        data = self.call("get_cartes", location, method="GET", params=params, schema=schemas.CARTE_SET_SCHEMA)
        return types.CarteSet(data)

    def get_comments_slice(
        self, posting_id: str, after: int | None = None, before: int | None = None, limit: int | None = None
    ) -> types.CommentsSliceInfo:
        location = "/postings/{postingId}/comments".format(postingId=quote_plus(posting_id))
        params = {"after": after, "before": before, "limit": limit}
        data = self.call(
            "get_comments_slice", location, method="GET", params=params, schema=schemas.COMMENTS_SLICE_INFO_SCHEMA,
            bodies=True
        )
        return types.CommentsSliceInfo(data)

    def create_comment(self, posting_id: str, comment: types.CommentText) -> types.CommentCreated:
        location = "/postings/{postingId}/comments".format(postingId=quote_plus(posting_id))
        data = self.call(
            "create_comment", location, method="POST", body=comment, schema=schemas.COMMENT_CREATED_SCHEMA, bodies=True
        )
        return types.CommentCreated(data)

    def get_comment(self, posting_id: str, comment_id: str, with_source: bool = False) -> types.CommentInfo:
        location = "/postings/{postingId}/comments/{commentId}".format(
            postingId=quote_plus(posting_id), commentId=quote_plus(comment_id)
        )
        include = comma_separated_flags({"source": with_source})
        params = {"include": include}
        data = self.call(
            "get_comment", location, method="GET", params=params, schema=schemas.COMMENT_INFO_SCHEMA, bodies=True
        )
        return types.CommentInfo(data)

    def update_all_comments(self, posting_id: str, attributes: types.CommentMassAttributes) -> types.Result:
        location = "/postings/{postingId}/comments".format(postingId=quote_plus(posting_id))
        data = self.call("update_all_comments", location, method="PUT", body=attributes, schema=schemas.RESULT_SCHEMA)
        return types.Result(data)

    def update_comment(self, posting_id: str, comment_id: str, comment: types.CommentText) -> types.CommentInfo:
        location = "/postings/{postingId}/comments/{commentId}".format(
            postingId=quote_plus(posting_id), commentId=quote_plus(comment_id)
        )
        data = self.call(
            "update_comment", location, method="PUT", body=comment, schema=schemas.COMMENT_INFO_SCHEMA, bodies=True
        )
        return types.CommentInfo(data)

    def delete_comment(self, posting_id: str, comment_id: str) -> types.CommentTotalInfo:
        location = "/postings/{postingId}/comments/{commentId}".format(
            postingId=quote_plus(posting_id), commentId=quote_plus(comment_id)
        )
        data = self.call("delete_comment", location, method="DELETE", schema=schemas.COMMENT_TOTAL_INFO_SCHEMA)
        return types.CommentTotalInfo(data)

    def get_postings_attached_to_comment(self, posting_id: str, comment_id: str) -> Sequence[types.PostingInfo]:
        location = "/postings/{postingId}/comments/{commentId}/attached".format(
            postingId=quote_plus(posting_id), commentId=quote_plus(comment_id)
        )
        data = self.call(
            "get_postings_attached_to_comment", location, method="GET", schema=schemas.POSTING_INFO_ARRAY_SCHEMA,
            bodies=True
        )
        return structure_list(data, types.PostingInfo)

    def get_comment_revisions(self, posting_id: str, comment_id: str) -> Sequence[types.CommentRevisionInfo]:
        location = "/postings/{postingId}/comments/{commentId}/revisions".format(
            postingId=quote_plus(posting_id), commentId=quote_plus(comment_id)
        )
        data = self.call(
            "get_comment_revisions", location, method="GET", schema=schemas.COMMENT_REVISION_INFO_ARRAY_SCHEMA,
            bodies=True
        )
        return structure_list(data, types.CommentRevisionInfo)

    def get_comment_revision(self, posting_id: str, comment_id: str, id: str) -> types.CommentRevisionInfo:
        location = "/postings/{postingId}/comments/{commentId}/revisions/{id}".format(
            postingId=quote_plus(posting_id), commentId=quote_plus(comment_id), id=quote_plus(id)
        )
        data = self.call(
            "get_comment_revision", location, method="GET", schema=schemas.COMMENT_REVISION_INFO_SCHEMA, bodies=True
        )
        return types.CommentRevisionInfo(data)

    def create_comment_reaction(
        self, posting_id: str, comment_id: str, reaction: types.ReactionDescription
    ) -> types.ReactionCreated:
        location = "/postings/{postingId}/comments/{commentId}/reactions".format(
            postingId=quote_plus(posting_id), commentId=quote_plus(comment_id)
        )
        data = self.call(
            "create_comment_reaction", location, method="POST", body=reaction, schema=schemas.REACTION_CREATED_SCHEMA
        )
        return types.ReactionCreated(data)

    def update_comment_reaction(
        self, posting_id: str, comment_id: str, owner_name: str, reaction: types.ReactionOverride
    ) -> types.ReactionInfo:
        location = "/postings/{postingId}/comments/{commentId}/reactions/{ownerName}".format(
            postingId=quote_plus(posting_id), commentId=quote_plus(comment_id), ownerName=quote_plus(owner_name)
        )
        data = self.call(
            "update_comment_reaction", location, method="PUT", body=reaction, schema=schemas.REACTION_INFO_SCHEMA
        )
        return types.ReactionInfo(data)

    def get_comment_reactions_slice(
        self, posting_id: str, comment_id: str, negative: bool | None = None, emoji: int | None = None,
        before: int | None = None, limit: int | None = None
    ) -> types.ReactionsSliceInfo:
        location = "/postings/{postingId}/comments/{commentId}/reactions".format(
            postingId=quote_plus(posting_id), commentId=quote_plus(comment_id)
        )
        params = {"negative": negative, "emoji": emoji, "before": before, "limit": limit}
        data = self.call(
            "get_comment_reactions_slice", location, method="GET", params=params,
            schema=schemas.REACTIONS_SLICE_INFO_SCHEMA
        )
        return types.ReactionsSliceInfo(data)

    def get_comment_reaction(self, posting_id: str, comment_id: str, owner_name: str) -> types.ReactionInfo:
        location = "/postings/{postingId}/comments/{commentId}/reactions/{ownerName}".format(
            postingId=quote_plus(posting_id), commentId=quote_plus(comment_id), ownerName=quote_plus(owner_name)
        )
        data = self.call("get_comment_reaction", location, method="GET", schema=schemas.REACTION_INFO_SCHEMA)
        return types.ReactionInfo(data)

    def delete_all_comment_reactions(self, posting_id: str, comment_id: str) -> types.Result:
        location = "/postings/{postingId}/comments/{commentId}/reactions".format(
            postingId=quote_plus(posting_id), commentId=quote_plus(comment_id)
        )
        data = self.call("delete_all_comment_reactions", location, method="DELETE", schema=schemas.RESULT_SCHEMA)
        return types.Result(data)

    def delete_comment_reaction(self, posting_id: str, comment_id: str, owner_name: str) -> types.ReactionTotalsInfo:
        location = "/postings/{postingId}/comments/{commentId}/reactions/{ownerName}".format(
            postingId=quote_plus(posting_id), commentId=quote_plus(comment_id), ownerName=quote_plus(owner_name)
        )
        data = self.call(
            "delete_comment_reaction", location, method="DELETE", schema=schemas.REACTION_TOTALS_INFO_SCHEMA
        )
        return types.ReactionTotalsInfo(data)

    def get_comment_reaction_totals(self, posting_id: str, comment_id: str) -> types.ReactionTotalsInfo:
        location = "/postings/{postingId}/comments/{commentId}/reaction-totals".format(
            postingId=quote_plus(posting_id), commentId=quote_plus(comment_id)
        )
        data = self.call(
            "get_comment_reaction_totals", location, method="GET", schema=schemas.REACTION_TOTALS_INFO_SCHEMA
        )
        return types.ReactionTotalsInfo(data)

    def get_contacts(self, query: str | None = None, limit: int | None = None) -> Sequence[types.ContactInfo]:
        location = "/people/contacts".format()
        params = {"query": query, "limit": limit}
        data = self.call(
            "get_contacts", location, method="GET", params=params, schema=schemas.CONTACT_INFO_ARRAY_SCHEMA
        )
        return structure_list(data, types.ContactInfo)

    def check_credentials(self) -> types.CredentialsCreated:
        location = "/credentials"
        data = self.call(
            "check_credentials", location, method="GET", auth=False, schema=schemas.CREDENTIALS_CREATED_SCHEMA
        )
        return types.CredentialsCreated(data)

    def create_credentials(self, credentials: types.Credentials) -> types.Result:
        location = "/credentials"
        data = self.call(
            "create_credentials", location, method="POST", body=credentials, auth=False, schema=schemas.RESULT_SCHEMA
        )
        return types.Result(data)

    def update_credentials(self, credentials: types.CredentialsChange) -> types.Result:
        location = "/credentials"
        data = self.call(
            "update_credentials", location, method="PUT", body=credentials, auth=False, schema=schemas.RESULT_SCHEMA
        )
        return types.Result(data)

    def delete_credentials(self) -> types.Result:
        location = "/credentials"
        data = self.call("delete_credentials", location, method="DELETE", schema=schemas.RESULT_SCHEMA)
        return types.Result(data)

    def reset_credentials(self) -> types.EmailHint:
        location = "/credentials/reset"
        data = self.call("reset_credentials", location, method="POST", auth=False, schema=schemas.EMAIL_HINT_SCHEMA)
        return types.EmailHint(data)

    def get_deleted_postings(self, page: int | None = None, limit: int | None = None) -> Sequence[types.PostingInfo]:
        location = "/deleted-postings".format()
        params = {"page": page, "limit": limit}
        data = self.call(
            "get_deleted_postings", location, method="GET", params=params, schema=schemas.POSTING_INFO_ARRAY_SCHEMA,
            bodies=True
        )
        return structure_list(data, types.PostingInfo)

    def get_deleted_posting(self, id: str) -> types.PostingInfo:
        location = "/deleted-postings/{id}".format(id=quote_plus(id))
        data = self.call(
            "get_deleted_posting", location, method="GET", schema=schemas.POSTING_INFO_SCHEMA, bodies=True
        )
        return types.PostingInfo(data)

    def restore_deleted_posting(self, id: str) -> types.PostingInfo:
        location = "/deleted-postings/{id}/restore".format(id=quote_plus(id))
        data = self.call(
            "restore_deleted_posting", location, method="POST", schema=schemas.POSTING_INFO_SCHEMA, bodies=True
        )
        return types.PostingInfo(data)

    def get_delete_posting_revisions(
        self, posting_id: str, limit: int | None = None
    ) -> Sequence[types.PostingRevisionInfo]:
        location = "/deleted-postings/{postingId}/revisions".format(postingId=quote_plus(posting_id))
        params = {"limit": limit}
        data = self.call(
            "get_delete_posting_revisions", location, method="GET", params=params,
            schema=schemas.POSTING_REVISION_INFO_ARRAY_SCHEMA, bodies=True
        )
        return structure_list(data, types.PostingRevisionInfo)

    def get_deleted_posting_revision(self, posting_id: str, id: str) -> types.PostingRevisionInfo:
        location = "/deleted-postings/{postingId}/revisions/{id}".format(
            postingId=quote_plus(posting_id), id=quote_plus(id)
        )
        data = self.call(
            "get_deleted_posting_revision", location, method="GET", schema=schemas.POSTING_REVISION_INFO_SCHEMA,
            bodies=True
        )
        return types.PostingRevisionInfo(data)

    def restore_deleted_posting_revision(self, posting_id: str, id: str) -> types.PostingRevisionInfo:
        location = "/postings/{postingId}/revisions/{id}/restore".format(
            postingId=quote_plus(posting_id), id=quote_plus(id)
        )
        data = self.call(
            "restore_deleted_posting_revision", location, method="POST", schema=schemas.POSTING_REVISION_INFO_SCHEMA,
            bodies=True
        )
        return types.PostingRevisionInfo(data)

    def get_domains(self) -> Sequence[types.DomainInfo]:
        location = "/domains"
        data = self.call("get_domains", location, method="GET", schema=schemas.DOMAIN_INFO_ARRAY_SCHEMA)
        return structure_list(data, types.DomainInfo)

    def get_domain(self, name: str) -> types.DomainInfo:
        location = "/domains/{name}".format(name=quote_plus(name))
        data = self.call("get_domain", location, method="GET", schema=schemas.DOMAIN_INFO_SCHEMA)
        return types.DomainInfo(data)

    def create_domain(self, domain: types.DomainAttributes) -> types.DomainInfo:
        location = "/domains"
        data = self.call("create_domain", location, method="POST", body=domain, schema=schemas.DOMAIN_INFO_SCHEMA)
        return types.DomainInfo(data)

    def update_domain(self, name: str, domain: types.DomainAttributes) -> types.DomainInfo:
        location = "/domains/{name}".format(name=quote_plus(name))
        data = self.call("update_domain", location, method="PUT", body=domain, schema=schemas.DOMAIN_INFO_SCHEMA)
        return types.DomainInfo(data)

    def delete_domain(self, name: str) -> types.Result:
        location = "/domains/{name}".format(name=quote_plus(name))
        data = self.call("delete_domain", location, method="DELETE", schema=schemas.RESULT_SCHEMA)
        return types.Result(data)

    def is_domain_available(self, node_name: str) -> types.DomainAvailable:
        location = "/domains/available".format()
        params = {"nodeName": node_name}
        data = self.call(
            "is_domain_available", location, method="GET", auth=False, params=params,
            schema=schemas.DOMAIN_AVAILABLE_SCHEMA
        )
        return types.DomainAvailable(data)

    def get_drafts(
        self, draft_type: types.DraftType, node_name: str, posting_id: str | None = None, comment_id: str | None = None,
        page: int | None = None, limit: int | None = None
    ) -> Sequence[types.DraftInfo]:
        location = "/drafts".format()
        params = {
            "draftType": draft_type, "nodeName": node_name, "postingId": posting_id, "commentId": comment_id,
            "page": page, "limit": limit
        }
        data = self.call(
            "get_drafts", location, method="GET", params=params, schema=schemas.DRAFT_INFO_ARRAY_SCHEMA, bodies=True
        )
        return structure_list(data, types.DraftInfo)

    def create_draft(self, draft: types.DraftText) -> types.DraftInfo:
        location = "/drafts"
        data = self.call(
            "create_draft", location, method="POST", body=draft, schema=schemas.DRAFT_INFO_SCHEMA, bodies=True
        )
        return types.DraftInfo(data)

    def get_draft(self, id: str) -> types.DraftInfo:
        location = "/drafts/{id}".format(id=quote_plus(id))
        data = self.call("get_draft", location, method="GET", schema=schemas.DRAFT_INFO_SCHEMA, bodies=True)
        return types.DraftInfo(data)

    def update_draft(self, id: str, draft: types.DraftText) -> types.DraftInfo:
        location = "/drafts/{id}".format(id=quote_plus(id))
        data = self.call(
            "update_draft", location, method="PUT", body=draft, schema=schemas.DRAFT_INFO_SCHEMA, bodies=True
        )
        return types.DraftInfo(data)

    def delete_draft(self, id: str) -> types.Result:
        location = "/draft/{id}".format(id=quote_plus(id))
        data = self.call("delete_draft", location, method="DELETE", schema=schemas.RESULT_SCHEMA)
        return types.Result(data)

    def get_features(self) -> types.Features:
        location = "/features"
        data = self.call("get_features", location, method="GET", schema=schemas.FEATURES_SCHEMA)
        return types.Features(data)

    def get_feeds(self) -> Sequence[types.FeedInfo]:
        location = "/feeds"
        data = self.call("get_feeds", location, method="GET", schema=schemas.FEED_INFO_ARRAY_SCHEMA)
        return structure_list(data, types.FeedInfo)

    def get_feed_general(self, feed_name: str) -> types.FeedInfo:
        location = "/feeds/{feedName}".format(feedName=quote_plus(feed_name))
        data = self.call("get_feed_general", location, method="GET", schema=schemas.FEED_INFO_SCHEMA)
        return types.FeedInfo(data)

    def get_feed_status(self, feed_name: str) -> types.FeedStatus:
        location = "/feeds/{feedName}/status".format(feedName=quote_plus(feed_name))
        data = self.call("get_feed_status", location, method="GET", schema=schemas.FEED_STATUS_SCHEMA)
        return types.FeedStatus(data)

    def update_feed_status(self, feed_name: str, change: types.FeedStatusChange) -> types.FeedStatus:
        location = "/feeds/{feedName}/status".format(feedName=quote_plus(feed_name))
        data = self.call("update_feed_status", location, method="PUT", body=change, schema=schemas.FEED_STATUS_SCHEMA)
        return types.FeedStatus(data)

    def get_feed_slice(
        self, feed_name: str, after: int | None = None, before: int | None = None, limit: int | None = None
    ) -> types.FeedSliceInfo:
        location = "/feeds/{feedName}/stories".format(feedName=quote_plus(feed_name))
        params = {"after": after, "before": before, "limit": limit}
        data = self.call(
            "get_feed_slice", location, method="GET", params=params, schema=schemas.FEED_SLICE_INFO_SCHEMA, bodies=True
        )
        return types.FeedSliceInfo(data)

    def get_friend_groups(self) -> Sequence[types.FriendGroupInfo]:
        location = "/people/friends/groups"
        data = self.call("get_friend_groups", location, method="GET", schema=schemas.FRIEND_GROUP_INFO_ARRAY_SCHEMA)
        return structure_list(data, types.FriendGroupInfo)

    def get_friend_group(self, id: str) -> types.FriendGroupInfo:
        location = "/people/friends/groups/{id}".format(id=quote_plus(id))
        data = self.call("get_friend_group", location, method="GET", schema=schemas.FRIEND_GROUP_INFO_SCHEMA)
        return types.FriendGroupInfo(data)

    def create_friend_group(self, friend_group: types.FriendGroupDescription) -> types.FriendGroupInfo:
        location = "/people/friends/groups"
        data = self.call(
            "create_friend_group", location, method="POST", body=friend_group, schema=schemas.FRIEND_GROUP_INFO_SCHEMA
        )
        return types.FriendGroupInfo(data)

    def update_friend_group(self, id: str, friend_group: types.FriendGroupDescription) -> types.FriendGroupInfo:
        location = "/people/friends/groups/{id}".format(id=quote_plus(id))
        data = self.call(
            "update_friend_group", location, method="PUT", body=friend_group, schema=schemas.FRIEND_GROUP_INFO_SCHEMA
        )
        return types.FriendGroupInfo(data)

    def delete_friend_group(self, id: str) -> types.Result:
        location = "/people/friends/groups/{id}".format(id=quote_plus(id))
        data = self.call("delete_friend_group", location, method="DELETE", schema=schemas.RESULT_SCHEMA)
        return types.Result(data)

    def get_friends(self, group_id: str | None = None) -> Sequence[types.FriendInfo]:
        location = "/people/friends".format()
        params = {"groupId": group_id}
        data = self.call("get_friends", location, method="GET", params=params, schema=schemas.FRIEND_INFO_ARRAY_SCHEMA)
        return structure_list(data, types.FriendInfo)

    def get_friend(self, name: str) -> types.FriendInfo:
        location = "/people/friends/{name}".format(name=quote_plus(name))
        data = self.call("get_friend", location, method="GET", schema=schemas.FRIEND_INFO_SCHEMA)
        return types.FriendInfo(data)

    def update_friends(self, friends: Sequence[types.FriendDescription]) -> Sequence[types.FriendInfo]:
        location = "/people/friends"
        data = self.call(
            "update_friends", location, method="PUT", body=friends, schema=schemas.FRIEND_INFO_ARRAY_SCHEMA
        )
        return structure_list(data, types.FriendInfo)

    def get_friend_ofs(self) -> Sequence[types.FriendOfInfo]:
        location = "/people/friend-ofs"
        data = self.call("get_friend_ofs", location, method="GET", schema=schemas.FRIEND_OF_INFO_ARRAY_SCHEMA)
        return structure_list(data, types.FriendOfInfo)

    def get_friend_of(self, name: str) -> types.FriendOfInfo:
        location = "/people/friend-ofs/{name}".format(name=quote_plus(name))
        data = self.call("get_friend_of", location, method="GET", schema=schemas.FRIEND_OF_INFO_SCHEMA)
        return types.FriendOfInfo(data)

    def upload_private_media(self, file: IO, file_type: str) -> types.PrivateMediaFileInfo:
        location = "/media/private"
        data = self.call(
            "upload_private_media", location, method="POST", body_file=file, body_file_type=file_type,
            schema=schemas.PRIVATE_MEDIA_FILE_INFO_SCHEMA
        )
        return types.PrivateMediaFileInfo(data)

    def get_private_media(self, id: str, width: int | None = None, download: bool | None = None) -> IO:
        location = "/media/private/{id}/data".format(id=quote_plus(id))
        params = {"width": width, "download": download}
        data = self.call("get_private_media", location, method="GET", params=params, schema="blob")
        return cast(IO, data)

    def get_private_media_info(self, id: str) -> types.PrivateMediaFileInfo:
        location = "/media/private/{id}/info".format(id=quote_plus(id))
        data = self.call(
            "get_private_media_info", location, method="GET", schema=schemas.PRIVATE_MEDIA_FILE_INFO_SCHEMA
        )
        return types.PrivateMediaFileInfo(data)

    def get_private_media_parent_entry(self, id: str) -> Sequence[types.EntryInfo]:
        location = "/media/private/{id}/parent".format(id=quote_plus(id))
        data = self.call(
            "get_private_media_parent_entry", location, method="GET", schema=schemas.ENTRY_INFO_ARRAY_SCHEMA,
            bodies=True
        )
        return structure_list(data, types.EntryInfo)

    def upload_public_media(self, file: IO, file_type: str) -> types.PublicMediaFileInfo:
        location = "/media/public"
        data = self.call(
            "upload_public_media", location, method="POST", body_file=file, body_file_type=file_type,
            schema=schemas.PUBLIC_MEDIA_FILE_INFO_SCHEMA
        )
        return types.PublicMediaFileInfo(data)

    def get_public_media(self, id: str, width: int | None = None, download: bool | None = None) -> IO:
        location = "/media/public/{id}/data".format(id=quote_plus(id))
        params = {"width": width, "download": download}
        data = self.call("get_public_media", location, method="GET", auth=False, params=params, schema="blob")
        return cast(IO, data)

    def get_public_media_info(self, id: str) -> types.PublicMediaFileInfo:
        location = "/media/public/{id}/info".format(id=quote_plus(id))
        data = self.call(
            "get_public_media_info", location, method="GET", auth=False, schema=schemas.PUBLIC_MEDIA_FILE_INFO_SCHEMA
        )
        return types.PublicMediaFileInfo(data)

    def get_node_name(self) -> types.NodeNameInfo:
        location = "/node-name"
        data = self.call("get_node_name", location, method="GET", auth=False, schema=schemas.NODE_NAME_INFO_SCHEMA)
        return types.NodeNameInfo(data)

    def create_node_name(self, name_to_register: types.NameToRegister) -> types.RegisteredNameSecret:
        location = "/node-name"
        data = self.call(
            "create_node_name", location, method="POST", body=name_to_register,
            schema=schemas.REGISTERED_NAME_SECRET_SCHEMA
        )
        return types.RegisteredNameSecret(data)

    def update_node_name(self, secret: types.RegisteredNameSecret) -> types.Result:
        location = "/node-name"
        data = self.call("update_node_name", location, method="PUT", body=secret, schema=schemas.RESULT_SCHEMA)
        return types.Result(data)

    def delete_node_name(self) -> types.Result:
        location = "/node-name"
        data = self.call("delete_node_name", location, method="DELETE", schema=schemas.RESULT_SCHEMA)
        return types.Result(data)

    def send_notification(self, packet: types.NotificationPacket) -> types.Result:
        location = "/notifications"
        data = self.call(
            "send_notification", location, method="POST", body=packet, auth=False, schema=schemas.RESULT_SCHEMA
        )
        return types.Result(data)

    def get_people_general(self) -> types.PeopleGeneralInfo:
        location = "/people"
        data = self.call("get_people_general", location, method="GET", schema=schemas.PEOPLE_GENERAL_INFO_SCHEMA)
        return types.PeopleGeneralInfo(data)

    def register_plugin(self, plugin: types.PluginDescription) -> types.PluginInfo:
        location = "/plugins"
        data = self.call("register_plugin", location, method="POST", body=plugin, schema=schemas.PLUGIN_INFO_SCHEMA)
        return types.PluginInfo(data)

    def get_plugins(self) -> Sequence[types.PluginInfo]:
        location = "/plugins"
        data = self.call("get_plugins", location, method="GET", schema=schemas.PLUGIN_INFO_ARRAY_SCHEMA)
        return structure_list(data, types.PluginInfo)

    def get_plugin(self, plugin_name: str) -> types.PluginInfo:
        location = "/plugins/{pluginName}".format(pluginName=quote_plus(plugin_name))
        data = self.call("get_plugin", location, method="GET", schema=schemas.PLUGIN_INFO_SCHEMA)
        return types.PluginInfo(data)

    def unregister_plugin(self, plugin_name: str) -> types.Result:
        location = "/plugins/{pluginName}".format(pluginName=quote_plus(plugin_name))
        data = self.call("unregister_plugin", location, method="DELETE", schema=schemas.RESULT_SCHEMA)
        return types.Result(data)

    def create_posting(self, posting: types.PostingText) -> types.PostingInfo:
        location = "/postings"
        data = self.call(
            "create_posting", location, method="POST", body=posting, schema=schemas.POSTING_INFO_SCHEMA, bodies=True
        )
        return types.PostingInfo(data)

    def update_posting(self, id: str, posting: types.PostingText) -> types.PostingInfo:
        location = "/postings/{id}".format(id=quote_plus(id))
        data = self.call(
            "update_posting", location, method="PUT", body=posting, schema=schemas.POSTING_INFO_SCHEMA, bodies=True
        )
        return types.PostingInfo(data)

    def get_posting(self, id: str, with_source: bool = False) -> types.PostingInfo:
        location = "/postings/{id}".format(id=quote_plus(id))
        include = comma_separated_flags({"source": with_source})
        params = {"include": include}
        data = self.call(
            "get_posting", location, method="GET", params=params, schema=schemas.POSTING_INFO_SCHEMA, bodies=True
        )
        return types.PostingInfo(data)

    def delete_posting(self, id: str) -> types.Result:
        location = "/postings/{id}".format(id=quote_plus(id))
        data = self.call("delete_posting", location, method="DELETE", schema=schemas.RESULT_SCHEMA)
        return types.Result(data)

    def get_postings_attached_to_posting(self, id: str) -> Sequence[types.PostingInfo]:
        location = "/postings/{id}/attached".format(id=quote_plus(id))
        data = self.call(
            "get_postings_attached_to_posting", location, method="GET", schema=schemas.POSTING_INFO_ARRAY_SCHEMA,
            bodies=True
        )
        return structure_list(data, types.PostingInfo)

    def get_posting_revisions(self, posting_id: str, limit: int | None = None) -> Sequence[types.PostingRevisionInfo]:
        location = "/postings/{postingId}/revisions".format(postingId=quote_plus(posting_id))
        params = {"limit": limit}
        data = self.call(
            "get_posting_revisions", location, method="GET", params=params,
            schema=schemas.POSTING_REVISION_INFO_ARRAY_SCHEMA, bodies=True
        )
        return structure_list(data, types.PostingRevisionInfo)

    def get_posting_revision(self, posting_id: str, id: str) -> types.PostingRevisionInfo:
        location = "/postings/{postingId}/revisions/{id}".format(postingId=quote_plus(posting_id), id=quote_plus(id))
        data = self.call(
            "get_posting_revision", location, method="GET", schema=schemas.POSTING_REVISION_INFO_SCHEMA, bodies=True
        )
        return types.PostingRevisionInfo(data)

    def restore_posting_revision(self, posting_id: str, id: str) -> types.PostingRevisionInfo:
        location = "/postings/{postingId}/revisions/{id}/restore".format(
            postingId=quote_plus(posting_id), id=quote_plus(id)
        )
        data = self.call(
            "restore_posting_revision", location, method="POST", schema=schemas.POSTING_REVISION_INFO_SCHEMA,
            bodies=True
        )
        return types.PostingRevisionInfo(data)

    def create_posting_reaction(self, posting_id: str, reaction: types.ReactionDescription) -> types.ReactionCreated:
        location = "/postings/{postingId}/reactions".format(postingId=quote_plus(posting_id))
        data = self.call(
            "create_posting_reaction", location, method="POST", body=reaction, schema=schemas.REACTION_CREATED_SCHEMA
        )
        return types.ReactionCreated(data)

    def get_posting_reactions_slice(
        self, posting_id: str, negative: bool | None = None, emoji: int | None = None, before: int | None = None,
        limit: int | None = None
    ) -> types.ReactionsSliceInfo:
        location = "/postings/{postingId}/reactions".format(postingId=quote_plus(posting_id))
        params = {"negative": negative, "emoji": emoji, "before": before, "limit": limit}
        data = self.call(
            "get_posting_reactions_slice", location, method="GET", params=params,
            schema=schemas.REACTIONS_SLICE_INFO_SCHEMA
        )
        return types.ReactionsSliceInfo(data)

    def update_posting_reaction(
        self, posting_id: str, owner_name: str, reaction: types.ReactionOverride
    ) -> types.ReactionInfo:
        location = "/postings/{postingId}/reactions/{ownerName}".format(
            postingId=quote_plus(posting_id), ownerName=quote_plus(owner_name)
        )
        data = self.call(
            "update_posting_reaction", location, method="PUT", body=reaction, schema=schemas.REACTION_INFO_SCHEMA
        )
        return types.ReactionInfo(data)

    def get_posting_reaction(self, posting_id: str, owner_name: str) -> types.ReactionInfo:
        location = "/postings/{postingId}/reactions/{ownerName}".format(
            postingId=quote_plus(posting_id), ownerName=quote_plus(owner_name)
        )
        data = self.call("get_posting_reaction", location, method="GET", schema=schemas.REACTION_INFO_SCHEMA)
        return types.ReactionInfo(data)

    def delete_all_posting_reactions(self, posting_id: str) -> types.Result:
        location = "/postings/{postingId}/reactions".format(postingId=quote_plus(posting_id))
        data = self.call("delete_all_posting_reactions", location, method="DELETE", schema=schemas.RESULT_SCHEMA)
        return types.Result(data)

    def delete_posting_reaction(self, posting_id: str, owner_name: str) -> types.ReactionTotalsInfo:
        location = "/postings/{postingId}/reactions/{ownerName}".format(
            postingId=quote_plus(posting_id), ownerName=quote_plus(owner_name)
        )
        data = self.call(
            "delete_posting_reaction", location, method="DELETE", schema=schemas.REACTION_TOTALS_INFO_SCHEMA
        )
        return types.ReactionTotalsInfo(data)

    def search_posting_reactions(self, filter: types.ReactionsFilter) -> Sequence[types.ReactionInfo]:
        location = "/postings/reactions/search"
        data = self.call(
            "search_posting_reactions", location, method="POST", body=filter, schema=schemas.REACTION_INFO_ARRAY_SCHEMA
        )
        return structure_list(data, types.ReactionInfo)

    def get_posting_reaction_totals(self, posting_id: str) -> types.ReactionTotalsInfo:
        location = "/postings/{postingId}/reaction-totals".format(postingId=quote_plus(posting_id))
        data = self.call(
            "get_posting_reaction_totals", location, method="GET", schema=schemas.REACTION_TOTALS_INFO_SCHEMA
        )
        return types.ReactionTotalsInfo(data)

    def search_posting_reaction_totals(
        self, filter: types.ReactionTotalsFilter
    ) -> Sequence[types.ReactionTotalsInfo]:
        location = "/postings/reaction-totals/search"
        data = self.call(
            "search_posting_reaction_totals", location, method="POST", body=filter,
            schema=schemas.REACTION_TOTALS_INFO_ARRAY_SCHEMA
        )
        return structure_list(data, types.ReactionTotalsInfo)

    def get_profile(self, with_source: bool = False) -> types.ProfileInfo:
        location = "/profile".format()
        include = comma_separated_flags({"source": with_source})
        params = {"include": include}
        data = self.call("get_profile", location, method="GET", params=params, schema=schemas.PROFILE_INFO_SCHEMA)
        return types.ProfileInfo(data)

    def update_profile(self, profile: types.ProfileAttributes) -> types.ProfileInfo:
        location = "/profile"
        data = self.call("update_profile", location, method="PUT", body=profile, schema=schemas.PROFILE_INFO_SCHEMA)
        return types.ProfileInfo(data)

    def proxy_media(self, url: str) -> IO:
        location = "/proxy/media".format()
        params = {"url": url}
        data = self.call("proxy_media", location, method="GET", params=params, schema="blob")
        return cast(IO, data)

    def proxy_link_preview(self, url: str) -> types.LinkPreviewInfo:
        location = "/proxy/link-preview".format()
        params = {"url": url}
        data = self.call(
            "proxy_link_preview", location, method="GET", params=params, schema=schemas.LINK_PREVIEW_INFO_SCHEMA
        )
        return types.LinkPreviewInfo(data)

    def ask_remote_node(self, node_name: str, details: types.AskDescription) -> types.Result:
        location = "/nodes/{nodeName}/ask".format(nodeName=quote_plus(node_name))
        data = self.call("ask_remote_node", location, method="POST", body=details, schema=schemas.RESULT_SCHEMA)
        return types.Result(data)

    def create_remote_comment(
        self, node_name: str, posting_id: str, comment: types.CommentSourceText
    ) -> types.Result:
        location = "/nodes/{nodeName}/postings/{postingId}/comments".format(
            nodeName=quote_plus(node_name), postingId=quote_plus(posting_id)
        )
        data = self.call("create_remote_comment", location, method="POST", body=comment, schema=schemas.RESULT_SCHEMA)
        return types.Result(data)

    def update_remote_comment(
        self, node_name: str, posting_id: str, comment_id: str, comment: types.CommentSourceText
    ) -> types.Result:
        location = "/nodes/{nodeName}/postings/{postingId}/comments/{commentId}".format(
            nodeName=quote_plus(node_name), postingId=quote_plus(posting_id), commentId=quote_plus(comment_id)
        )
        data = self.call("update_remote_comment", location, method="PUT", body=comment, schema=schemas.RESULT_SCHEMA)
        return types.Result(data)

    def delete_remote_comment(self, node_name: str, posting_id: str, comment_id: str) -> types.Result:
        location = "/nodes/{nodeName}/postings/{postingId}/comments/{commentId}".format(
            nodeName=quote_plus(node_name), postingId=quote_plus(posting_id), commentId=quote_plus(comment_id)
        )
        data = self.call("delete_remote_comment", location, method="DELETE", schema=schemas.RESULT_SCHEMA)
        return types.Result(data)

    def verify_remote_comment(self, node_name: str, posting_id: str, comment_id: str) -> types.AsyncOperationCreated:
        location = "/nodes/{nodeName}/postings/{postingId}/comments/{commentId}/verify".format(
            nodeName=quote_plus(node_name), postingId=quote_plus(posting_id), commentId=quote_plus(comment_id)
        )
        data = self.call(
            "verify_remote_comment", location, method="POST", schema=schemas.ASYNC_OPERATION_CREATED_SCHEMA
        )
        return types.AsyncOperationCreated(data)

    def create_remote_comment_reaction(
        self, node_name: str, posting_id: str, comment_id: str, reaction: types.ReactionAttributes
    ) -> types.Result:
        location = "/nodes/{nodeName}/postings/{postingId}/comments/{commentId}/reactions".format(
            nodeName=quote_plus(node_name), postingId=quote_plus(posting_id), commentId=quote_plus(comment_id)
        )
        data = self.call(
            "create_remote_comment_reaction", location, method="POST", body=reaction, schema=schemas.RESULT_SCHEMA
        )
        return types.Result(data)

    def delete_remote_comment_reaction(self, node_name: str, posting_id: str, comment_id: str) -> types.Result:
        location = "/nodes/{nodeName}/postings/{postingId}/comments/{commentId}/reactions".format(
            nodeName=quote_plus(node_name), postingId=quote_plus(posting_id), commentId=quote_plus(comment_id)
        )
        data = self.call("delete_remote_comment_reaction", location, method="DELETE", schema=schemas.RESULT_SCHEMA)
        return types.Result(data)

    def verify_remote_comment_reaction(
        self, node_name: str, posting_id: str, comment_id: str, owner_name: str
    ) -> types.AsyncOperationCreated:
        location = "/nodes/{nodeName}/postings/{postingId}/comments/{commentId}/reactions/{ownerName}/verify".format(
            nodeName=quote_plus(node_name), postingId=quote_plus(posting_id), commentId=quote_plus(comment_id),
            ownerName=quote_plus(owner_name)
        )
        data = self.call(
            "verify_remote_comment_reaction", location, method="POST", schema=schemas.ASYNC_OPERATION_CREATED_SCHEMA
        )
        return types.AsyncOperationCreated(data)

    def create_remote_posting(self, node_name: str, posting: types.PostingSourceText) -> types.Result:
        location = "/nodes/{nodeName}/postings".format(nodeName=quote_plus(node_name))
        data = self.call("create_remote_posting", location, method="POST", body=posting, schema=schemas.RESULT_SCHEMA)
        return types.Result(data)

    def update_remote_posting(
        self, node_name: str, posting_id: str, posting: types.PostingSourceText
    ) -> types.Result:
        location = "/nodes/{nodeName}/postings/{postingId}".format(
            nodeName=quote_plus(node_name), postingId=quote_plus(posting_id)
        )
        data = self.call("update_remote_posting", location, method="PUT", body=posting, schema=schemas.RESULT_SCHEMA)
        return types.Result(data)

    def delete_remote_posting(self, node_name: str, posting_id: str) -> types.Result:
        location = "/nodes/{nodeName}/postings/{postingId}".format(
            nodeName=quote_plus(node_name), postingId=quote_plus(posting_id)
        )
        data = self.call("delete_remote_posting", location, method="DELETE", schema=schemas.RESULT_SCHEMA)
        return types.Result(data)

    def verify_remote_posting(self, node_name: str, id: str) -> types.AsyncOperationCreated:
        location = "/nodes/{nodeName}/postings/{id}/verify".format(nodeName=quote_plus(node_name), id=quote_plus(id))
        data = self.call(
            "verify_remote_posting", location, method="POST", schema=schemas.ASYNC_OPERATION_CREATED_SCHEMA
        )
        return types.AsyncOperationCreated(data)

    def verify_remote_posting_revision(
        self, node_name: str, id: str, revision_id: str
    ) -> types.AsyncOperationCreated:
        location = "/nodes/{nodeName}/postings/{id}/revisions/{revisionId}/verify".format(
            nodeName=quote_plus(node_name), id=quote_plus(id), revisionId=quote_plus(revision_id)
        )
        data = self.call(
            "verify_remote_posting_revision", location, method="POST", schema=schemas.ASYNC_OPERATION_CREATED_SCHEMA
        )
        return types.AsyncOperationCreated(data)

    def create_remote_posting_reaction(
        self, node_name: str, posting_id: str, reaction: types.ReactionAttributes
    ) -> types.Result:
        location = "/nodes/{nodeName}/postings/{postingId}/reactions".format(
            nodeName=quote_plus(node_name), postingId=quote_plus(posting_id)
        )
        data = self.call(
            "create_remote_posting_reaction", location, method="POST", body=reaction, schema=schemas.RESULT_SCHEMA
        )
        return types.Result(data)

    def delete_remote_posting_reaction(self, node_name: str, posting_id: str) -> types.Result:
        location = "/nodes/{nodeName}/postings/{postingId}/reactions".format(
            nodeName=quote_plus(node_name), postingId=quote_plus(posting_id)
        )
        data = self.call("delete_remote_posting_reaction", location, method="DELETE", schema=schemas.RESULT_SCHEMA)
        return types.Result(data)

    def verify_remote_posting_reaction(
        self, node_name: str, posting_id: str, owner_name: str
    ) -> types.AsyncOperationCreated:
        location = "/nodes/{nodeName}/postings/{postingId}/reactions/{ownerName}/verify".format(
            nodeName=quote_plus(node_name), postingId=quote_plus(posting_id), ownerName=quote_plus(owner_name)
        )
        data = self.call(
            "verify_remote_posting_reaction", location, method="POST", schema=schemas.ASYNC_OPERATION_CREATED_SCHEMA
        )
        return types.AsyncOperationCreated(data)

    def create_remote_sheriff_order(
        self, node_name: str, sheriff_order: types.SheriffOrderAttributes
    ) -> types.Result:
        location = "/nodes/{nodeName}/sheriff/orders".format(nodeName=quote_plus(node_name))
        data = self.call(
            "create_remote_sheriff_order", location, method="POST", body=sheriff_order, schema=schemas.RESULT_SCHEMA
        )
        return types.Result(data)

    def get_remote_sheriff_order(self, node_name: str, id: str) -> types.SheriffOrderInfo:
        location = "/nodes/{nodeName}/sheriff/orders/{id}".format(nodeName=quote_plus(node_name), id=quote_plus(id))
        data = self.call(
            "get_remote_sheriff_order", location, method="GET", auth=False, schema=schemas.SHERIFF_ORDER_INFO_SCHEMA
        )
        return types.SheriffOrderInfo(data)

    def update_settings(self, settings: Sequence[types.SettingInfo]) -> types.Result:
        location = "/settings"
        data = self.call("update_settings", location, method="PUT", body=settings, schema=schemas.RESULT_SCHEMA)
        return types.Result(data)

    def get_client_settings(self, prefix: str | None = None) -> Sequence[types.SettingInfo]:
        location = "/settings/client".format()
        params = {"prefix": prefix}
        data = self.call(
            "get_client_settings", location, method="GET", params=params, schema=schemas.SETTING_INFO_ARRAY_SCHEMA
        )
        return structure_list(data, types.SettingInfo)

    def get_node_settings(self, prefix: str | None = None) -> Sequence[types.SettingInfo]:
        location = "/settings/node".format()
        params = {"prefix": prefix}
        data = self.call(
            "get_node_settings", location, method="GET", params=params, schema=schemas.SETTING_INFO_ARRAY_SCHEMA
        )
        return structure_list(data, types.SettingInfo)

    def get_node_settings_metadata(self, prefix: str | None = None) -> Sequence[types.SettingMetaInfo]:
        location = "/settings/node/metadata".format()
        params = {"prefix": prefix}
        data = self.call(
            "get_node_settings_metadata", location, method="GET", params=params,
            schema=schemas.SETTING_META_INFO_ARRAY_SCHEMA
        )
        return structure_list(data, types.SettingMetaInfo)

    def update_node_settings_metadata(self, metadata: Sequence[types.SettingMetaAttributes]) -> types.Result:
        location = "/settings/node/metadata"
        data = self.call(
            "update_node_settings_metadata", location, method="PUT", body=metadata, schema=schemas.RESULT_SCHEMA
        )
        return types.Result(data)

    def get_sheriff_complaint_groups_slice(
        self, after: int | None = None, before: int | None = None, limit: int | None = None,
        status: types.SheriffComplainStatus | None = None
    ) -> types.SheriffComplainGroupsSliceInfo:
        location = "/sheriff/complains/groups".format()
        params = {"after": after, "before": before, "limit": limit, "status": status}
        data = self.call(
            "get_sheriff_complaint_groups_slice", location, method="GET", auth=False, params=params,
            schema=schemas.SHERIFF_COMPLAIN_GROUPS_SLICE_INFO_SCHEMA
        )
        return types.SheriffComplainGroupsSliceInfo(data)

    def get_sheriff_complaint_group(self, id: str) -> types.SheriffComplainGroupInfo:
        location = "/sheriff/complains/groups/{id}".format(id=quote_plus(id))
        data = self.call(
            "get_sheriff_complaint_group", location, method="GET", auth=False,
            schema=schemas.SHERIFF_COMPLAIN_GROUP_INFO_SCHEMA
        )
        return types.SheriffComplainGroupInfo(data)

    def get_sheriff_complaints_by_group(self, id: str) -> Sequence[types.SheriffComplainInfo]:
        location = "/sheriff/complains/groups/{id}/complains".format(id=quote_plus(id))
        data = self.call(
            "get_sheriff_complaints_by_group", location, method="GET", auth=False,
            schema=schemas.SHERIFF_COMPLAIN_INFO_ARRAY_SCHEMA
        )
        return structure_list(data, types.SheriffComplainInfo)

    def update_sheriff_complaint_group(
        self, id: str, decision: types.SheriffComplainDecisionText
    ) -> types.SheriffComplainGroupInfo:
        location = "/sheriff/complains/groups/{id}".format(id=quote_plus(id))
        data = self.call(
            "update_sheriff_complaint_group", location, method="PUT", body=decision,
            schema=schemas.SHERIFF_COMPLAIN_GROUP_INFO_SCHEMA
        )
        return types.SheriffComplainGroupInfo(data)

    def create_sheriff_complaint(self, complaint: types.SheriffComplainText) -> types.SheriffComplainInfo:
        location = "/sheriff/complains"
        data = self.call(
            "create_sheriff_complaint", location, method="POST", body=complaint,
            schema=schemas.SHERIFF_COMPLAIN_INFO_SCHEMA
        )
        return types.SheriffComplainInfo(data)

    def create_sheriff_order(self, sheriff_order: types.SheriffOrderDetails) -> types.Result:
        location = "/sheriff/orders"
        data = self.call(
            "create_sheriff_order", location, method="POST", body=sheriff_order, auth=False,
            schema=schemas.RESULT_SCHEMA
        )
        return types.Result(data)

    def get_story(self, id: str) -> types.StoryInfo:
        location = "/stories/{id}".format(id=quote_plus(id))
        data = self.call("get_story", location, method="GET", schema=schemas.STORY_INFO_SCHEMA, bodies=True)
        return types.StoryInfo(data)

    def update_story(self, id: str, story: types.StoryAttributes) -> types.StoryInfo:
        location = "/stories/{id}".format(id=quote_plus(id))
        data = self.call(
            "update_story", location, method="PUT", body=story, schema=schemas.STORY_INFO_SCHEMA, bodies=True
        )
        return types.StoryInfo(data)

    def get_subscribers(
        self, node_name: str | None = None, type: types.SubscriptionType | None = None, feed_name: str | None = None,
        entry_id: str | None = None
    ) -> Sequence[types.SubscriberInfo]:
        location = "/people/subscribers".format()
        params = {"nodeName": node_name, "type": type, "feedName": feed_name, "entryId": entry_id}
        data = self.call(
            "get_subscribers", location, method="GET", params=params, schema=schemas.SUBSCRIBER_INFO_ARRAY_SCHEMA
        )
        return structure_list(data, types.SubscriberInfo)

    def create_subscriber(self, subscriber: types.SubscriberDescription) -> types.SubscriberInfo:
        location = "/people/subscribers"
        data = self.call(
            "create_subscriber", location, method="POST", body=subscriber, schema=schemas.SUBSCRIBER_INFO_SCHEMA
        )
        return types.SubscriberInfo(data)

    def get_subscriber(self, id: str) -> types.SubscriberInfo:
        location = "/people/subscribers/{id}".format(id=quote_plus(id))
        data = self.call("get_subscriber", location, method="GET", schema=schemas.SUBSCRIBER_INFO_SCHEMA)
        return types.SubscriberInfo(data)

    def update_subscriber(self, id: str, subscriber: types.SubscriberOverride) -> types.SubscriberInfo:
        location = "/people/subscribers/{id}".format(id=quote_plus(id))
        data = self.call(
            "update_subscriber", location, method="PUT", body=subscriber, schema=schemas.SUBSCRIBER_INFO_SCHEMA
        )
        return types.SubscriberInfo(data)

    def delete_subscriber(self, id: str) -> types.ContactInfo:
        location = "/people/subscribers/{id}".format(id=quote_plus(id))
        data = self.call("delete_subscriber", location, method="DELETE", schema=schemas.CONTACT_INFO_SCHEMA)
        return types.ContactInfo(data)

    def get_subscriptions(
        self, node_name: str | None = None, type: types.SubscriptionType | None = None
    ) -> Sequence[types.SubscriptionInfo]:
        location = "/people/subscriptions".format()
        params = {"nodeName": node_name, "type": type}
        data = self.call(
            "get_subscriptions", location, method="GET", params=params, schema=schemas.SUBSCRIPTION_INFO_ARRAY_SCHEMA
        )
        return structure_list(data, types.SubscriptionInfo)

    def create_subscription(self, subscription: types.SubscriptionDescription) -> types.SubscriptionInfo:
        location = "/people/subscriptions"
        data = self.call(
            "create_subscription", location, method="POST", body=subscription, schema=schemas.SUBSCRIPTION_INFO_SCHEMA
        )
        return types.SubscriptionInfo(data)

    def update_subscription(self, id: str, subscription: types.SubscriptionOverride) -> types.SubscriptionInfo:
        location = "/people/subscriptions/{id}".format(id=quote_plus(id))
        data = self.call(
            "update_subscription", location, method="PUT", body=subscription, schema=schemas.SUBSCRIPTION_INFO_SCHEMA
        )
        return types.SubscriptionInfo(data)

    def delete_subscription(self, id: str) -> types.ContactInfo:
        location = "/people/subscriptions/{id}".format(id=quote_plus(id))
        data = self.call("delete_subscription", location, method="DELETE", schema=schemas.CONTACT_INFO_SCHEMA)
        return types.ContactInfo(data)

    def search_subscriptions(self, filter: types.SubscriptionFilter) -> Sequence[types.SubscriptionInfo]:
        location = "/people/subscriptions/search"
        data = self.call(
            "search_subscriptions", location, method="GET", body=filter, schema=schemas.SUBSCRIPTION_INFO_ARRAY_SCHEMA
        )
        return structure_list(data, types.SubscriptionInfo)

    def get_tokens(self) -> Sequence[types.TokenInfo]:
        location = "/tokens"
        data = self.call("get_tokens", location, method="GET", schema=schemas.TOKEN_INFO_ARRAY_SCHEMA)
        return structure_list(data, types.TokenInfo)

    def create_token(self, token: types.TokenAttributes) -> types.TokenInfo:
        location = "/tokens"
        data = self.call(
            "create_token", location, method="POST", body=token, auth=False, schema=schemas.TOKEN_INFO_SCHEMA
        )
        return types.TokenInfo(data)

    def get_token_info(self, id: str) -> types.TokenInfo:
        location = "/tokens/{id}".format(id=quote_plus(id))
        data = self.call("get_token_info", location, method="GET", schema=schemas.TOKEN_INFO_SCHEMA)
        return types.TokenInfo(data)

    def update_token(self, id: str, token: types.TokenName) -> types.TokenInfo:
        location = "/tokens/{id}".format(id=quote_plus(id))
        data = self.call("update_token", location, method="PUT", body=token, schema=schemas.TOKEN_INFO_SCHEMA)
        return types.TokenInfo(data)

    def delete_token(self, id: str) -> types.Result:
        location = "/tokens/{id}".format(id=quote_plus(id))
        data = self.call("delete_token", location, method="DELETE", schema=schemas.RESULT_SCHEMA)
        return types.Result(data)

    def get_user_list_general(self, name: str) -> types.UserListInfo:
        location = "/user-lists/{name}".format(name=quote_plus(name))
        data = self.call(
            "get_user_list_general", location, method="GET", auth=False, schema=schemas.USER_LIST_INFO_SCHEMA
        )
        return types.UserListInfo(data)

    def get_user_list_slice(
        self, name: str, after: int | None = None, before: int | None = None, limit: int | None = None
    ) -> types.UserListSliceInfo:
        location = "/user-lists/{name}/items".format(name=quote_plus(name))
        params = {"after": after, "before": before, "limit": limit}
        data = self.call(
            "get_user_list_slice", location, method="GET", auth=False, params=params,
            schema=schemas.USER_LIST_SLICE_INFO_SCHEMA
        )
        return types.UserListSliceInfo(data)

    def get_user_list_item(self, name: str, node_name: str) -> types.UserListItemInfo:
        location = "/user-lists/{name}/items/{nodeName}".format(name=quote_plus(name), nodeName=quote_plus(node_name))
        data = self.call(
            "get_user_list_item", location, method="GET", auth=False, schema=schemas.USER_LIST_ITEM_INFO_SCHEMA
        )
        return types.UserListItemInfo(data)

    def create_user_list_item(self, name: str, item: types.UserListItemAttributes) -> types.UserListItemInfo:
        location = "/user-lists/{name}/items".format(name=quote_plus(name))
        data = self.call(
            "create_user_list_item", location, method="POST", body=item, schema=schemas.USER_LIST_ITEM_INFO_SCHEMA
        )
        return types.UserListItemInfo(data)

    def delete_user_list_item(self, name: str, node_name: str) -> types.Result:
        location = "/user-lists/{name}/items/{nodeName}".format(name=quote_plus(name), nodeName=quote_plus(node_name))
        data = self.call("delete_user_list_item", location, method="DELETE", schema=schemas.RESULT_SCHEMA)
        return types.Result(data)

    def who_am_i(self) -> types.WhoAmI:
        location = "/whoami"
        data = self.call("who_am_i", location, method="GET", auth=False, schema=schemas.WHO_AM_I_SCHEMA)
        return types.WhoAmI(data)
