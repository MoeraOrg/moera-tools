# This file is generated

from typing import Literal, Mapping, Sequence, TypeAlias

from moeralib.structure import Structure

Timestamp: TypeAlias = int
PrincipalValue: TypeAlias = str

AskSubject = Literal["subscribe", "friend"]

BlockedEntryOperation = Literal["addComment", "addReaction"]

BlockedOperation = Literal["reaction", "comment", "posting", "visibility", "instant"]

BodyFormat = Literal["message", "application"]

DraftType = Literal["new-posting", "posting-update", "new-comment", "comment-update"]

OperationStatus = Literal["waiting", "added", "started", "succeeded", "failed", "unknown"]

PrincipalFlag = Literal[
    "none", "private", "admin", "owner", "secret", "senior", "enigma", "major", "signed", "subscribed", "public",
    "friends", "unset"
]

PushContentType = Literal["story-added", "story-deleted", "feed-updated"]

SettingType = Literal[
    "bool", "int", "string", "json", "Duration", "PrivateKey", "PublicKey", "Timestamp", "UUID", "Principal"
]

SheriffComplainStatus = Literal[
    "posted", "prepared", "prepare-failed", "not-found", "invalid-target", "not-original", "not-sheriff", "approved",
    "rejected"
]

SheriffOrderCategory = Literal["visibility"]

SheriffOrderReason = Literal[
    "unlawful", "defamatory", "threat", "spam", "scam", "malware", "copyright", "impersonating", "privacy", "other"
]

SourceFormat = Literal["plain-text", "html", "markdown", "application"]

StoryType = Literal[
    "asked-to-friend", "asked-to-subscribe", "blocked-user", "blocked-user-in-posting", "comment-added",
    "comment-media-reaction-added-negative", "comment-media-reaction-added-positive", "comment-media-reaction-failed",
    "comment-post-task-failed", "comment-reaction-added-negative", "comment-reaction-added-positive",
    "comment-reaction-task-failed", "comment-update-task-failed", "friend-added", "friend-deleted",
    "friend-group-deleted", "mention-comment", "mention-posting", "posting-added",
    "posting-media-reaction-added-negative", "posting-media-reaction-added-positive", "posting-media-reaction-failed",
    "posting-post-task-failed", "posting-reaction-task-failed", "posting-subscribe-task-failed",
    "posting-update-task-failed", "posting-updated", "reaction-added-negative", "reaction-added-positive",
    "remote-comment-added", "reply-comment", "sheriff-complain-added", "sheriff-complain-decided", "sheriff-marked",
    "sheriff-unmarked", "subscriber-added", "subscriber-deleted", "unblocked-user", "unblocked-user-in-posting"
]

SubscriptionReason = Literal["user", "mention", "comment"]

SubscriptionType = Literal["feed", "posting", "posting-comments", "profile", "user-list"]

VerificationStatus = Literal["running", "correct", "incorrect", "error"]


class CommentOperations(Structure):
    view: PrincipalValue | None = None
    edit: PrincipalValue | None = None
    delete: PrincipalValue | None = None
    view_reactions: PrincipalValue | None = None
    view_negative_reactions: PrincipalValue | None = None
    view_reaction_totals: PrincipalValue | None = None
    view_negative_reaction_totals: PrincipalValue | None = None
    view_reaction_ratios: PrincipalValue | None = None
    view_negative_reaction_ratios: PrincipalValue | None = None
    add_reaction: PrincipalValue | None = None
    add_negative_reaction: PrincipalValue | None = None


class ContactOperations(Structure):
    view_feed_subscriber: PrincipalValue | None = None
    view_feed_subscription: PrincipalValue | None = None
    view_friend: PrincipalValue | None = None
    view_friend_of: PrincipalValue | None = None
    view_block: PrincipalValue | None = None
    view_block_by: PrincipalValue | None = None


class FeedOperations(Structure):
    add: PrincipalValue | None = None


class FriendOperations(Structure):
    view: PrincipalValue | None = None


class FriendGroupOperations(Structure):
    view: PrincipalValue | None = None


class NodeNameOperations(Structure):
    manage: PrincipalValue | None = None


class PeopleOperations(Structure):
    view_subscribers: PrincipalValue | None = None
    view_subscriptions: PrincipalValue | None = None
    view_friends: PrincipalValue | None = None
    view_friend_ofs: PrincipalValue | None = None
    view_blocked: PrincipalValue | None = None
    view_blocked_by: PrincipalValue | None = None
    view_subscribers_total: PrincipalValue | None = None
    view_subscriptions_total: PrincipalValue | None = None
    view_friends_total: PrincipalValue | None = None
    view_friend_ofs_total: PrincipalValue | None = None


class PostingOperations(Structure):
    view: PrincipalValue | None = None
    edit: PrincipalValue | None = None
    delete: PrincipalValue | None = None
    view_comments: PrincipalValue | None = None
    add_comment: PrincipalValue | None = None
    override_comment: PrincipalValue | None = None
    view_reactions: PrincipalValue | None = None
    view_negative_reactions: PrincipalValue | None = None
    view_reaction_totals: PrincipalValue | None = None
    view_negative_reaction_totals: PrincipalValue | None = None
    view_reaction_ratios: PrincipalValue | None = None
    view_negative_reaction_ratios: PrincipalValue | None = None
    add_reaction: PrincipalValue | None = None
    add_negative_reaction: PrincipalValue | None = None
    override_reaction: PrincipalValue | None = None
    override_comment_reaction: PrincipalValue | None = None


class PrivateMediaFileOperations(Structure):
    view: PrincipalValue | None = None


class ProfileOperations(Structure):
    edit: PrincipalValue | None = None
    view_email: PrincipalValue | None = None


class ReactionOperations(Structure):
    view: PrincipalValue | None = None
    delete: PrincipalValue | None = None


class StoryOperations(Structure):
    edit: PrincipalValue | None = None
    delete: PrincipalValue | None = None


class SubscriberOperations(Structure):
    view: PrincipalValue | None = None
    delete: PrincipalValue | None = None


class SubscriptionOperations(Structure):
    view: PrincipalValue | None = None
    delete: PrincipalValue | None = None


class AcceptedReactions(Structure):
    positive: str
    negative: str


class AskDescription(Structure):
    subject: AskSubject
    friend_group_id: str | None = None
    message: str | None = None


class AsyncOperationCreated(Structure):
    id: str


class AvatarAttributes(Structure):
    media_id: str
    clip_x: int
    clip_y: int
    clip_size: int
    avatar_size: int
    rotate: float
    shape: str | None = None
    ordinal: int | None = None


class AvatarDescription(Structure):
    media_id: str
    shape: str
    optional: bool | None = None


class AvatarImage(Structure):
    media_id: str
    path: str
    width: int | None = None
    height: int | None = None
    shape: str | None = None


class AvatarInfo(Structure):
    id: str
    media_id: str
    path: str
    width: int | None = None
    height: int | None = None
    shape: str | None = None
    ordinal: int


class AvatarOrdinal(Structure):
    id: str
    ordinal: int


class AvatarsOrdered(Structure):
    ids: Sequence[str]


class BlockedInstantAttributes(Structure):
    story_type: StoryType
    entry_id: str | None = None
    remote_node_name: str | None = None
    remote_posting_id: str | None = None
    remote_owner_name: str | None = None
    deadline: Timestamp | None = None


class BlockedInstantFilter(Structure):
    story_type: StoryType
    entry_id: str | None = None
    remote_node_name: str | None = None
    remote_posting_id: str | None = None
    remote_owner_name: str | None = None


class BlockedInstantInfo(Structure):
    id: str
    story_type: StoryType
    entry_id: str | None = None
    remote_node_name: str | None = None
    remote_posting_id: str | None = None
    remote_owner_name: str | None = None
    created_at: Timestamp
    deadline: Timestamp | None = None


class BlockedPostingInstantInfo(Structure):
    id: str
    story_type: StoryType
    remote_owner_name: str | None = None
    deadline: Timestamp | None = None


class BlockedUserAttributes(Structure):
    blocked_operation: BlockedOperation
    node_name: str
    entry_id: str | None = None
    entry_node_name: str | None = None
    entry_posting_id: str | None = None
    deadline: Timestamp | None = None
    reason_src: str | None = None
    reason_src_format: SourceFormat | None = None


class BlockedUserFilter(Structure):
    blocked_operations: Sequence[BlockedOperation] | None = None
    node_name: str | None = None
    entry_id: str | None = None
    entry_node_name: str | None = None
    entry_posting_id: str | None = None
    strict: bool | None = None


class BlockedUsersChecksums(Structure):
    visibility: int


class CarteInfo(Structure):
    carte: str
    beginning: Timestamp
    deadline: Timestamp
    permissions: Sequence[str] | None = None


class CarteSet(Structure):
    cartes_ip: str | None = None
    cartes: Sequence[CarteInfo]
    created_at: Timestamp


class ClientReactionInfo(Structure):
    negative: bool
    emoji: int
    created_at: Timestamp
    deadline: Timestamp | None = None


class CommentMassAttributes(Structure):
    senior_operations: CommentOperations | None = None


class CommentTotalInfo(Structure):
    total: int


class ContactInfo(Structure):
    node_name: str
    full_name: str | None = None
    gender: str | None = None
    avatar: AvatarImage | None = None
    closeness: float
    has_feed_subscriber: bool | None = None
    has_feed_subscription: bool | None = None
    has_friend: bool | None = None
    has_friend_of: bool | None = None
    has_block: bool | None = None
    has_block_by: bool | None = None
    operations: ContactOperations | None = None
    owner_operations: ContactOperations | None = None
    admin_operations: ContactOperations | None = None


class Credentials(Structure):
    login: str
    password: str


class CredentialsChange(Structure):
    token: str | None = None
    old_password: str | None = None
    login: str
    password: str


class CredentialsCreated(Structure):
    created: bool


class DomainAttributes(Structure):
    name: str | None = None
    node_id: str | None = None


class DomainAvailable(Structure):
    name: str


class DomainInfo(Structure):
    name: str
    node_id: str
    created_at: Timestamp


class EmailHint(Structure):
    email_hint: str


class FeedReference(Structure):
    feed_name: str
    published_at: Timestamp
    pinned: bool | None = None
    moment: int
    story_id: str
    operations: StoryOperations | None = None


class FeedStatus(Structure):
    total: int
    total_pinned: int
    last_moment: int | None = None
    not_viewed: int | None = None
    not_read: int | None = None
    not_viewed_moment: int | None = None
    not_read_moment: int | None = None


class FeedStatusChange(Structure):
    viewed: bool | None = None
    read: bool | None = None
    before: int


class FeedWithStatus(Structure):
    feed_name: str
    not_viewed: int
    not_read: int


class FriendGroupAssignment(Structure):
    id: str
    operations: FriendOperations | None = None


class FriendGroupDescription(Structure):
    title: str
    operations: FriendGroupOperations | None = None


class FriendGroupDetails(Structure):
    id: str
    title: str | None = None
    added_at: Timestamp
    operations: FriendOperations | None = None


class FriendGroupInfo(Structure):
    id: str
    title: str | None = None
    created_at: Timestamp
    operations: FriendGroupOperations | None = None


class FriendGroupsFeatures(Structure):
    available: Sequence[FriendGroupInfo]
    member_of: Sequence[FriendGroupDetails] | None = None


class FriendInfo(Structure):
    node_name: str
    contact: ContactInfo | None = None
    groups: Sequence[FriendGroupDetails] | None = None


class FriendOfInfo(Structure):
    remote_node_name: str
    contact: ContactInfo | None = None
    groups: Sequence[FriendGroupDetails] | None = None


class FundraiserInfo(Structure):
    title: str
    qr_code: str | None = None
    text: str | None = None
    href: str | None = None


class LinkPreview(Structure):
    site_name: str | None = None
    url: str | None = None
    title: str | None = None
    description: str | None = None
    image_hash: str | None = None


class LinkPreviewInfo(Structure):
    site_name: str | None = None
    url: str | None = None
    title: str | None = None
    description: str | None = None
    image_url: str | None = None


class MediaFilePreviewInfo(Structure):
    target_width: int
    width: int
    height: int
    original: bool | None = None


class MediaWithDigest(Structure):
    id: str
    digest: str | None = None


class NameToRegister(Structure):
    name: str


class NotificationPacket(Structure):
    id: str
    node_name: str
    full_name: str | None = None
    gender: str | None = None
    avatar: AvatarImage | None = None
    created_at: Timestamp
    type: str
    notification: str
    signature: bytes
    signature_version: int


class NodeNameInfo(Structure):
    name: str | None = None
    operation_status: OperationStatus | None = None
    operation_status_updated: Timestamp | None = None
    operation_error_code: str | None = None
    operation_error_message: str | None = None
    operations: NodeNameOperations | None = None


class PeopleGeneralInfo(Structure):
    feed_subscribers_total: int | None = None
    feed_subscriptions_total: int | None = None
    friends_total: Mapping[str, int] | None = None
    friend_ofs_total: int | None = None
    blocked_total: int | None = None
    blocked_by_total: int | None = None
    operations: PeopleOperations | None = None


class PluginContext(Structure):
    root_admin: bool
    admin: bool
    auth_categories: Sequence[str]
    client_name: str
    remote_address: str
    user_agent: str
    user_agent_os: str
    node_id: str
    node_name: str
    domain_name: str
    origin_url: str


class PostingFeatures(Structure):
    post: bool | None = None
    subject_present: bool
    source_formats: Sequence[SourceFormat]
    media_max_size: int
    image_recommended_size: int
    image_recommended_pixels: int
    image_formats: Sequence[str]


class PostingSourceInfo(Structure):
    node_name: str
    full_name: str | None = None
    avatar: AvatarImage | None = None
    feed_name: str
    posting_id: str
    created_at: Timestamp


class PrivateMediaFileInfo(Structure):
    id: str
    hash: str
    path: str
    mime_type: str
    width: int | None = None
    height: int | None = None
    orientation: int | None = None
    size: int
    posting_id: str | None = None
    previews: Sequence[MediaFilePreviewInfo] | None = None
    operations: PrivateMediaFileOperations | None = None


class ProfileAttributes(Structure):
    full_name: str | None = None
    gender: str | None = None
    email: str | None = None
    title: str | None = None
    bio_src: str | None = None
    bio_src_format: SourceFormat | None = None
    avatar_id: str | None = None
    fundraisers: Sequence[FundraiserInfo] | None = None
    operations: ProfileOperations | None = None


class ProfileInfo(Structure):
    full_name: str | None = None
    gender: str | None = None
    email: str | None = None
    title: str | None = None
    bio_src: str | None = None
    bio_src_format: SourceFormat | None = None
    bio_html: str | None = None
    avatar: AvatarInfo | None = None
    fundraisers: Sequence[FundraiserInfo] | None = None
    operations: ProfileOperations | None = None


class PublicMediaFileInfo(Structure):
    id: str
    path: str
    width: int | None = None
    height: int | None = None
    orientation: int | None = None
    size: int


class ReactionAttributes(Structure):
    negative: bool
    emoji: int
    operations: ReactionOperations | None = None


class ReactionDescription(Structure):
    owner_name: str | None = None
    owner_full_name: str | None = None
    owner_gender: str | None = None
    owner_avatar: AvatarDescription | None = None
    negative: bool
    emoji: int
    signature: bytes | None = None
    signature_version: int | None = None
    operations: ReactionOperations | None = None


class ReactionsFilter(Structure):
    owner_name: str | None = None
    postings: Sequence[str] | None = None


class ReactionInfo(Structure):
    owner_name: str | None = None
    owner_full_name: str | None = None
    owner_gender: str | None = None
    owner_avatar: AvatarImage | None = None
    posting_id: str | None = None
    posting_revision_id: str | None = None
    comment_id: str | None = None
    comment_revision_id: str | None = None
    negative: bool | None = None
    emoji: int | None = None
    moment: int | None = None
    created_at: Timestamp | None = None
    deadline: Timestamp | None = None
    signature: bytes | None = None
    signature_version: int | None = None
    operations: ReactionOperations | None = None
    owner_operations: ReactionOperations | None = None
    senior_operations: ReactionOperations | None = None
    major_operations: ReactionOperations | None = None


class ReactionsSliceInfo(Structure):
    before: int
    after: int
    total: int
    reactions: Sequence[ReactionInfo]


class ReactionTotalInfo(Structure):
    emoji: int
    total: int | None = None
    share: float | None = None


class ReactionTotalsFilter(Structure):
    postings: Sequence[str]


class ReactionTotalsInfo(Structure):
    entry_id: str
    positive: Sequence[ReactionTotalInfo] | None = None
    negative: Sequence[ReactionTotalInfo] | None = None


class ReactionOverride(Structure):
    operations: ReactionOperations | None = None
    senior_operations: ReactionOperations | None = None
    major_operations: ReactionOperations | None = None


class RegisteredNameSecret(Structure):
    name: str
    mnemonic: Sequence[str] | None = None
    secret: str | None = None


class RemoteFeed(Structure):
    node_name: str
    feed_name: str


class RemoteMedia(Structure):
    id: str
    hash: str | None = None
    digest: str | None = None


class RemoteMediaInfo(Structure):
    id: str
    hash: str | None = None
    digest: str | None = None


class RemotePosting(Structure):
    node_name: str
    posting_id: str


class RemotePostingOrNode(Structure):
    node_name: str
    posting_id: str | None = None


class RemotePostingVerificationInfo(Structure):
    id: str
    node_name: str
    posting_id: str
    revision_id: str | None = None
    status: VerificationStatus | None = None
    error_code: str | None = None
    error_message: str | None = None


class RemoteReactionVerificationInfo(Structure):
    id: str
    node_name: str
    posting_id: str
    reaction_owner_name: str
    status: VerificationStatus | None = None
    error_code: str | None = None
    error_message: str | None = None


class RepliedTo(Structure):
    id: str
    revision_id: str | None = None
    name: str
    full_name: str | None = None
    gender: str | None = None
    avatar: AvatarImage | None = None
    heading: str | None = None
    digest: bytes


class Result(Structure):
    error_code: str
    message: str | None = None


class SheriffMark(Structure):
    sheriff_name: str


class SettingInfo(Structure):
    name: str
    value: str | None = None


class SettingMetaAttributes(Structure):
    name: str
    default_value: str | None = None
    privileged: bool | None = None


class SettingTypeModifiers(Structure):
    format: str | None = None
    min: str | None = None
    max: str | None = None
    multiline: bool | None = None
    never: bool | None = None
    always: bool | None = None
    principals: Sequence[PrincipalFlag] | None = None


class SheriffComplainDecisionText(Structure):
    reject: bool
    decision_code: SheriffOrderReason | None = None
    decision_details: str | None = None
    anonymous: bool | None = None


class SheriffComplainGroupInfo(Structure):
    id: str
    remote_node_name: str
    remote_node_full_name: str | None = None
    remote_feed_name: str
    remote_posting_id: str | None = None
    remote_posting_revision_id: str | None = None
    remote_posting_owner_name: str | None = None
    remote_posting_owner_full_name: str | None = None
    remote_posting_owner_gender: str | None = None
    remote_posting_heading: str | None = None
    remote_comment_id: str | None = None
    remote_comment_revision_id: str | None = None
    remote_comment_owner_name: str | None = None
    remote_comment_owner_full_name: str | None = None
    remote_comment_owner_gender: str | None = None
    remote_comment_heading: str | None = None
    created_at: Timestamp
    moment: int
    status: SheriffComplainStatus
    decision_code: SheriffOrderReason | None = None
    decision_details: str | None = None
    decided_at: Timestamp | None = None
    anonymous: bool | None = None


class SheriffComplainGroupsSliceInfo(Structure):
    before: int
    after: int
    groups: Sequence[SheriffComplainGroupInfo]
    total: int
    total_in_past: int
    total_in_future: int


class SheriffComplainInfo(Structure):
    id: str
    owner_name: str
    owner_full_name: str | None = None
    owner_gender: str | None = None
    group: SheriffComplainGroupInfo | None = None
    reason_code: SheriffOrderReason
    reason_details: str | None = None
    anonymous_requested: bool | None = None
    created_at: Timestamp


class SheriffComplainText(Structure):
    owner_full_name: str | None = None
    owner_gender: str | None = None
    node_name: str
    full_name: str | None = None
    feed_name: str
    posting_id: str | None = None
    posting_owner_name: str | None = None
    posting_owner_full_name: str | None = None
    posting_owner_gender: str | None = None
    posting_heading: str | None = None
    comment_id: str | None = None
    comment_owner_name: str | None = None
    comment_owner_full_name: str | None = None
    comment_owner_gender: str | None = None
    comment_heading: str | None = None
    reason_code: SheriffOrderReason | None = None
    reason_details: str | None = None
    anonymous: bool | None = None


class SheriffOrderAttributes(Structure):
    delete: bool | None = None
    feed_name: str
    posting_id: str | None = None
    comment_id: str | None = None
    category: SheriffOrderCategory
    reason_code: SheriffOrderReason | None = None
    reason_details: str | None = None


class SheriffOrderDetails(Structure):
    id: str
    delete: bool | None = None
    sheriff_name: str
    sheriff_avatar: AvatarDescription | None = None
    feed_name: str
    posting_id: str | None = None
    comment_id: str | None = None
    category: SheriffOrderCategory
    reason_code: SheriffOrderReason | None = None
    reason_details: str | None = None
    created_at: Timestamp
    signature: bytes
    signature_version: int


class SheriffOrderInfo(Structure):
    id: str
    delete: bool | None = None
    sheriff_name: str
    node_name: str
    node_full_name: str | None = None
    feed_name: str
    posting_id: str | None = None
    posting_revision_id: str | None = None
    posting_owner_name: str | None = None
    posting_owner_full_name: str | None = None
    posting_owner_gender: str | None = None
    posting_heading: str | None = None
    comment_id: str | None = None
    comment_revision_id: str | None = None
    comment_owner_name: str | None = None
    comment_owner_full_name: str | None = None
    comment_owner_gender: str | None = None
    comment_heading: str | None = None
    category: SheriffOrderCategory
    reason_code: SheriffOrderReason | None = None
    reason_details: str | None = None
    created_at: Timestamp
    signature: bytes
    signature_version: int
    complain_group_id: str | None = None


class StoryAttributes(Structure):
    feed_name: str | None = None
    publish_at: Timestamp | None = None
    pinned: bool | None = None
    viewed: bool | None = None
    read: bool | None = None
    satisfied: bool | None = None


class StorySummaryBlocked(Structure):
    operations: Sequence[BlockedOperation]
    period: int | None = None


class StorySummaryFriendGroup(Structure):
    id: str | None = None
    title: str | None = None


class StorySummaryEntry(Structure):
    owner_name: str | None = None
    owner_full_name: str | None = None
    owner_gender: str | None = None
    heading: str | None = None
    sheriffs: Sequence[str] | None = None
    sheriff_marks: Sequence[SheriffMark] | None = None


class StorySummaryNode(Structure):
    owner_name: str | None = None
    owner_full_name: str | None = None
    owner_gender: str | None = None


class StorySummaryReaction(Structure):
    owner_name: str | None = None
    owner_full_name: str | None = None
    owner_gender: str | None = None
    emoji: int | None = None


class StorySummarySheriff(Structure):
    sheriff_name: str
    order_id: str | None = None
    complain_id: str | None = None


class SubscriberDescription(Structure):
    type: SubscriptionType
    feed_name: str | None = None
    posting_id: str | None = None
    last_updated_at: Timestamp | None = None
    operations: SubscriberOperations | None = None


class SubscriberInfo(Structure):
    id: str
    type: SubscriptionType
    feed_name: str | None = None
    posting_id: str | None = None
    node_name: str
    contact: ContactInfo | None = None
    created_at: Timestamp
    operations: SubscriberOperations | None = None
    owner_operations: SubscriberOperations | None = None
    admin_operations: SubscriberOperations | None = None


class SubscriberOverride(Structure):
    operations: SubscriberOperations | None = None
    admin_operations: SubscriberOperations | None = None


class SubscriptionDescription(Structure):
    type: SubscriptionType
    feed_name: str | None = None
    remote_node_name: str
    remote_feed_name: str | None = None
    remote_posting_id: str | None = None
    reason: SubscriptionReason | None = None
    operations: SubscriptionOperations | None = None


class SubscriptionFilter(Structure):
    type: SubscriptionType | None = None
    feeds: Sequence[RemoteFeed] | None = None
    postings: Sequence[RemotePosting] | None = None


class SubscriptionInfo(Structure):
    id: str
    type: SubscriptionType
    feed_name: str | None = None
    remote_node_name: str
    contact: ContactInfo | None = None
    remote_feed_name: str | None = None
    remote_posting_id: str | None = None
    created_at: Timestamp
    reason: SubscriptionReason
    operations: SubscriptionOperations | None = None


class SubscriptionOverride(Structure):
    operations: SubscriptionOperations | None = None


class TokenAttributes(Structure):
    login: str
    password: str
    auth_category: int | None = None
    name: str | None = None


class TokenInfo(Structure):
    id: str
    token: str
    name: str | None = None
    permissions: Sequence[str] | None = None
    plugin_name: str | None = None
    created_at: Timestamp
    deadline: Timestamp | None = None
    last_used_at: Timestamp | None = None
    last_used_browser: str | None = None
    last_used_ip: str | None = None


class TokenName(Structure):
    name: str | None = None


class UpdateInfo(Structure):
    important: bool | None = None
    description: str | None = None


class UserListInfo(Structure):
    name: str
    total: int


class UserListItemAttributes(Structure):
    node_name: str


class UserListItemInfo(Structure):
    node_name: str
    created_at: Timestamp
    moment: int


class UserListSliceInfo(Structure):
    list_name: str
    before: int
    after: int
    items: Sequence[UserListItemInfo]
    total: int
    total_in_past: int
    total_in_future: int


class WhoAmI(Structure):
    node_name: str | None = None
    node_name_changing: bool | None = None
    full_name: str | None = None
    gender: str | None = None
    title: str | None = None
    avatar: AvatarImage | None = None


class ActivityReactionFilter(Structure):
    postings: Sequence[RemotePosting] | None = None


class ActivityReactionInfo(Structure):
    remote_node_name: str
    remote_full_name: str | None = None
    remote_avatar: AvatarImage | None = None
    remote_posting_id: str
    negative: bool
    emoji: int
    created_at: Timestamp


class BlockedByUserFilter(Structure):
    blocked_operations: Sequence[BlockedOperation] | None = None
    postings: Sequence[RemotePostingOrNode] | None = None
    strict: bool | None = None


class BlockedByUserInfo(Structure):
    id: str
    blocked_operation: BlockedOperation
    contact: ContactInfo | None = None
    node_name: str
    posting_id: str | None = None
    created_at: Timestamp
    deadline: Timestamp | None = None
    reason: str | None = None


class BlockedUserInfo(Structure):
    id: str
    blocked_operation: BlockedOperation
    node_name: str
    contact: ContactInfo | None = None
    entry_id: str | None = None
    entry_node_name: str | None = None
    entry_posting_id: str | None = None
    created_at: Timestamp
    deadline: Timestamp | None = None
    reason_src: str | None = None
    reason_src_format: SourceFormat | None = None
    reason: str | None = None


class Body(Structure):
    subject: str | None = None
    text: str | None = None
    link_previews: Sequence[LinkPreview] | None = None


class CommentRevisionInfo(Structure):
    id: str
    posting_revision_id: str
    body_preview: Body | None = None
    body_src_hash: bytes
    body_src_format: SourceFormat | None = None
    body: Body
    body_format: BodyFormat | None = None
    heading: str
    created_at: Timestamp
    deleted_at: Timestamp | None = None
    deadline: Timestamp | None = None
    digest: bytes
    signature: bytes | None = None
    signature_version: int | None = None
    client_reaction: ClientReactionInfo | None = None
    reactions: ReactionTotalsInfo | None = None


class CommentSourceText(Structure):
    owner_avatar: AvatarDescription | None = None
    body_src: Body | None = None
    body_src_format: SourceFormat | None = None
    media: Sequence[MediaWithDigest] | None = None
    accepted_reactions: AcceptedReactions | None = None
    replied_to_id: str | None = None
    operations: CommentOperations | None = None
    senior_operations: CommentOperations | None = None


class CommentText(Structure):
    owner_name: str | None = None
    owner_full_name: str | None = None
    owner_gender: str | None = None
    owner_avatar: AvatarDescription | None = None
    body_preview: Body | None = None
    body_src: Body | None = None
    body_src_format: SourceFormat | None = None
    body: Body | None = None
    body_format: BodyFormat | None = None
    media: Sequence[str] | None = None
    created_at: Timestamp | None = None
    accepted_reactions: AcceptedReactions | None = None
    replied_to_id: str | None = None
    signature: bytes | None = None
    signature_version: int | None = None
    operations: CommentOperations | None = None
    reaction_operations: ReactionOperations | None = None
    senior_operations: CommentOperations | None = None


class DraftText(Structure):
    draft_type: DraftType
    receiver_name: str
    receiver_posting_id: str | None = None
    receiver_comment_id: str | None = None
    replied_to_id: str | None = None
    owner_full_name: str | None = None
    owner_avatar: AvatarDescription | None = None
    accepted_reactions: AcceptedReactions | None = None
    body_src: Body | None = None
    body_src_format: SourceFormat | None = None
    media: Sequence[RemoteMedia] | None = None
    publish_at: int | None = None
    update_info: UpdateInfo | None = None
    operations: PostingOperations | None = None
    comment_operations: CommentOperations | None = None


class Features(Structure):
    posting: PostingFeatures
    plugins: Sequence[str] | None = None
    feed_width: int
    friend_groups: FriendGroupsFeatures | None = None
    ask: Sequence[AskSubject] | None = None
    subscribed: bool | None = None


class FeedInfo(Structure):
    feed_name: str
    title: str | None = None
    total: int
    first_created_at: Timestamp | None = None
    last_created_at: Timestamp | None = None
    operations: FeedOperations | None = None
    sheriffs: Sequence[str] | None = None
    sheriff_marks: Sequence[SheriffMark] | None = None


class FriendDescription(Structure):
    node_name: str
    groups: Sequence[FriendGroupAssignment] | None = None


class MediaAttachment(Structure):
    media: PrivateMediaFileInfo | None = None
    remote_media: RemoteMediaInfo | None = None
    embedded: bool


class PostingInfo(Structure):
    id: str
    revision_id: str
    receiver_revision_id: str | None = None
    total_revisions: int
    receiver_name: str | None = None
    receiver_full_name: str | None = None
    receiver_gender: str | None = None
    receiver_avatar: AvatarImage | None = None
    receiver_posting_id: str | None = None
    parent_media_id: str | None = None
    owner_name: str
    owner_full_name: str | None = None
    owner_gender: str | None = None
    owner_avatar: AvatarImage | None = None
    body_preview: Body | None = None
    body_src: Body | None = None
    body_src_hash: bytes
    body_src_format: SourceFormat | None = None
    body: Body
    body_format: BodyFormat | None = None
    media: Sequence[MediaAttachment] | None = None
    heading: str
    update_info: UpdateInfo | None = None
    created_at: Timestamp
    edited_at: Timestamp | None = None
    deleted_at: Timestamp | None = None
    receiver_created_at: Timestamp | None = None
    receiver_edited_at: Timestamp | None = None
    receiver_deleted_at: Timestamp | None = None
    revision_created_at: Timestamp
    receiver_revision_created_at: Timestamp | None = None
    deadline: Timestamp | None = None
    digest: bytes
    signature: bytes | None = None
    signature_version: int | None = None
    feed_references: Sequence[FeedReference] | None = None
    blocked_instants: Sequence[BlockedPostingInstantInfo] | None = None
    operations: PostingOperations | None = None
    receiver_operations: PostingOperations | None = None
    comment_operations: CommentOperations | None = None
    reaction_operations: ReactionOperations | None = None
    comment_reaction_operations: ReactionOperations | None = None
    blocked_operations: Sequence[BlockedEntryOperation] | None = None
    blocked_comment_operations: Sequence[BlockedEntryOperation] | None = None
    sheriffs: Sequence[str] | None = None
    sheriff_marks: Sequence[SheriffMark] | None = None
    accepted_reactions: AcceptedReactions | None = None
    client_reaction: ClientReactionInfo | None = None
    reactions: ReactionTotalsInfo | None = None
    sources: Sequence[PostingSourceInfo] | None = None
    total_comments: int | None = None


class PostingRevisionInfo(Structure):
    id: str
    receiver_id: str | None = None
    body_preview: Body | None = None
    body_src_hash: bytes
    body_src_format: SourceFormat | None = None
    body: Body
    body_format: BodyFormat | None = None
    media: Sequence[MediaAttachment] | None = None
    heading: str
    update_info: UpdateInfo | None = None
    created_at: Timestamp
    deleted_at: Timestamp | None = None
    receiver_created_at: Timestamp | None = None
    receiver_deleted_at: Timestamp | None = None
    digest: bytes
    signature: bytes | None = None
    signature_version: int | None = None
    client_reaction: ClientReactionInfo | None = None
    reactions: ReactionTotalsInfo | None = None


class PostingSourceText(Structure):
    owner_avatar: AvatarDescription | None = None
    body_src: Body | None = None
    body_src_format: SourceFormat | None = None
    media: Sequence[MediaWithDigest] | None = None
    accepted_reactions: AcceptedReactions | None = None
    operations: PostingOperations | None = None
    comment_operations: CommentOperations | None = None


class PostingText(Structure):
    owner_name: str | None = None
    owner_full_name: str | None = None
    owner_gender: str | None = None
    owner_avatar: AvatarDescription | None = None
    body_preview: Body | None = None
    body_src: Body | None = None
    body_src_format: SourceFormat | None = None
    body: Body | None = None
    body_format: BodyFormat | None = None
    media: Sequence[str] | None = None
    created_at: Timestamp | None = None
    accepted_reactions: AcceptedReactions | None = None
    publications: Sequence[StoryAttributes] | None = None
    update_info: UpdateInfo | None = None
    signature: bytes | None = None
    signature_version: int | None = None
    operations: PostingOperations | None = None
    comment_operations: CommentOperations | None = None
    reaction_operations: ReactionOperations | None = None
    comment_reaction_operations: ReactionOperations | None = None


class ReactionCreated(Structure):
    reaction: ReactionInfo | None = None
    totals: ReactionTotalsInfo


class SettingDescriptor(Structure):
    name: str
    type: SettingType
    default_value: str | None = None
    internal: bool | None = None
    privileged: bool | None = None
    title: str | None = None
    modifiers: SettingTypeModifiers | None = None


class SettingMetaInfo(Structure):
    name: str
    type: SettingType
    default_value: str | None = None
    privileged: bool | None = None
    title: str
    modifiers: SettingTypeModifiers | None = None


class StorySummaryData(Structure):
    node: StorySummaryNode | None = None
    posting: StorySummaryEntry | None = None
    comment: StorySummaryEntry | None = None
    comments: Sequence[StorySummaryEntry] | None = None
    total_comments: int | None = None
    replied_to: StorySummaryEntry | None = None
    parent_posting: StorySummaryEntry | None = None
    reaction: StorySummaryReaction | None = None
    reactions: Sequence[StorySummaryReaction] | None = None
    total_reactions: int | None = None
    feed_name: str | None = None
    subscription_reason: SubscriptionReason | None = None
    friend_group: StorySummaryFriendGroup | None = None
    blocked: StorySummaryBlocked | None = None
    sheriff: StorySummarySheriff | None = None
    description: str | None = None


class CommentInfo(Structure):
    id: str
    owner_name: str
    owner_full_name: str | None = None
    owner_gender: str | None = None
    owner_avatar: AvatarImage | None = None
    posting_id: str
    posting_revision_id: str
    revision_id: str
    total_revisions: int
    body_preview: Body | None = None
    body_src: Body | None = None
    body_src_hash: bytes
    body_src_format: SourceFormat | None = None
    body: Body
    body_format: BodyFormat | None = None
    media: Sequence[MediaAttachment] | None = None
    heading: str
    replied_to: RepliedTo | None = None
    moment: int
    created_at: Timestamp
    edited_at: Timestamp | None = None
    deleted_at: Timestamp | None = None
    revision_created_at: Timestamp
    deadline: Timestamp | None = None
    digest: bytes
    signature: bytes | None = None
    signature_version: int | None = None
    operations: CommentOperations | None = None
    reaction_operations: ReactionOperations | None = None
    owner_operations: CommentOperations | None = None
    senior_operations: CommentOperations | None = None
    blocked_operations: Sequence[BlockedEntryOperation] | None = None
    sheriff_marks: Sequence[SheriffMark] | None = None
    accepted_reactions: AcceptedReactions | None = None
    client_reaction: ClientReactionInfo | None = None
    senior_reaction: ClientReactionInfo | None = None
    reactions: ReactionTotalsInfo | None = None


class CommentsSliceInfo(Structure):
    before: int
    after: int
    comments: Sequence[CommentInfo]
    total: int
    total_in_past: int
    total_in_future: int


class DraftInfo(Structure):
    id: str
    draft_type: DraftType
    receiver_name: str
    receiver_posting_id: str | None = None
    receiver_comment_id: str | None = None
    replied_to_id: str | None = None
    created_at: Timestamp
    edited_at: Timestamp | None = None
    deadline: Timestamp | None = None
    owner_full_name: str | None = None
    owner_avatar: AvatarImage | None = None
    accepted_reactions: AcceptedReactions | None = None
    body_src: Body | None = None
    body_src_format: SourceFormat | None = None
    body: Body
    body_format: BodyFormat | None = None
    media: Sequence[MediaAttachment] | None = None
    heading: str
    publish_at: int | None = None
    update_info: UpdateInfo | None = None
    operations: PostingOperations | None = None
    comment_operations: CommentOperations | None = None


class EntryInfo(Structure):
    posting: PostingInfo | None = None
    comment: CommentInfo | None = None


class PluginDescription(Structure):
    name: str
    title: str | None = None
    description: str | None = None
    location: str | None = None
    accepted_events: Sequence[str] | None = None
    options: Sequence[SettingDescriptor] | None = None


class PluginInfo(Structure):
    node_id: str
    local: bool
    name: str
    title: str | None = None
    description: str | None = None
    location: str | None = None
    accepted_events: Sequence[str] | None = None
    settings: Sequence[SettingMetaInfo] | None = None
    token_id: str | None = None


class StoryInfo(Structure):
    id: str
    feed_name: str
    story_type: StoryType
    created_at: Timestamp
    published_at: Timestamp
    pinned: bool | None = None
    moment: int
    viewed: bool | None = None
    read: bool | None = None
    satisfied: bool | None = None
    summary_node_name: str | None = None
    summary_full_name: str | None = None
    summary_avatar: AvatarImage | None = None
    summary: str | None = None
    summary_data: StorySummaryData | None = None
    tracking_id: str | None = None
    posting: PostingInfo | None = None
    posting_id: str | None = None
    comment: CommentInfo | None = None
    comment_id: str | None = None
    remote_node_name: str | None = None
    remote_full_name: str | None = None
    remote_posting_id: str | None = None
    remote_comment_id: str | None = None
    remote_media_id: str | None = None
    operations: StoryOperations | None = None


class CommentCreated(Structure):
    comment: CommentInfo
    total: int


class FeedSliceInfo(Structure):
    before: int
    after: int
    stories: Sequence[StoryInfo]
    total_in_past: int
    total_in_future: int


class PushContent(Structure):
    type: PushContentType
    id: str | None = None
    story: StoryInfo | None = None
    feed_status: FeedWithStatus | None = None
