# This file is generated

from typing import Any

from ..structure import to_nullable_object_schema, array_schema

COMMENT_OPERATIONS_SCHEMA: Any = {
    "type": "object",
    "properties": {
        "view": {
            "type": ["string", "null"]
        },
        "edit": {
            "type": ["string", "null"]
        },
        "delete": {
            "type": ["string", "null"]
        },
        "viewReactions": {
            "type": ["string", "null"]
        },
        "viewNegativeReactions": {
            "type": ["string", "null"]
        },
        "viewReactionTotals": {
            "type": ["string", "null"]
        },
        "viewNegativeReactionTotals": {
            "type": ["string", "null"]
        },
        "viewReactionRatios": {
            "type": ["string", "null"]
        },
        "viewNegativeReactionRatios": {
            "type": ["string", "null"]
        },
        "addReaction": {
            "type": ["string", "null"]
        },
        "addNegativeReaction": {
            "type": ["string", "null"]
        },
    },
    "additionalProperties": False
}

CONTACT_OPERATIONS_SCHEMA: Any = {
    "type": "object",
    "properties": {
        "viewFeedSubscriber": {
            "type": ["string", "null"]
        },
        "viewFeedSubscription": {
            "type": ["string", "null"]
        },
        "viewFriend": {
            "type": ["string", "null"]
        },
        "viewFriendOf": {
            "type": ["string", "null"]
        },
        "viewBlock": {
            "type": ["string", "null"]
        },
        "viewBlockBy": {
            "type": ["string", "null"]
        },
    },
    "additionalProperties": False
}

FEED_OPERATIONS_SCHEMA: Any = {
    "type": "object",
    "properties": {
        "add": {
            "type": ["string", "null"]
        },
    },
    "additionalProperties": False
}

FRIEND_OPERATIONS_SCHEMA: Any = {
    "type": "object",
    "properties": {
        "view": {
            "type": ["string", "null"]
        },
    },
    "additionalProperties": False
}

FRIEND_GROUP_OPERATIONS_SCHEMA: Any = {
    "type": "object",
    "properties": {
        "view": {
            "type": ["string", "null"]
        },
    },
    "additionalProperties": False
}

NODE_NAME_OPERATIONS_SCHEMA: Any = {
    "type": "object",
    "properties": {
        "manage": {
            "type": ["string", "null"]
        },
    },
    "additionalProperties": False
}

PEOPLE_OPERATIONS_SCHEMA: Any = {
    "type": "object",
    "properties": {
        "viewSubscribers": {
            "type": ["string", "null"]
        },
        "viewSubscriptions": {
            "type": ["string", "null"]
        },
        "viewFriends": {
            "type": ["string", "null"]
        },
        "viewFriendOfs": {
            "type": ["string", "null"]
        },
        "viewBlocked": {
            "type": ["string", "null"]
        },
        "viewBlockedBy": {
            "type": ["string", "null"]
        },
        "viewSubscribersTotal": {
            "type": ["string", "null"]
        },
        "viewSubscriptionsTotal": {
            "type": ["string", "null"]
        },
        "viewFriendsTotal": {
            "type": ["string", "null"]
        },
        "viewFriendOfsTotal": {
            "type": ["string", "null"]
        },
    },
    "additionalProperties": False
}

POSTING_OPERATIONS_SCHEMA: Any = {
    "type": "object",
    "properties": {
        "view": {
            "type": ["string", "null"]
        },
        "edit": {
            "type": ["string", "null"]
        },
        "delete": {
            "type": ["string", "null"]
        },
        "viewComments": {
            "type": ["string", "null"]
        },
        "addComment": {
            "type": ["string", "null"]
        },
        "overrideComment": {
            "type": ["string", "null"]
        },
        "viewReactions": {
            "type": ["string", "null"]
        },
        "viewNegativeReactions": {
            "type": ["string", "null"]
        },
        "viewReactionTotals": {
            "type": ["string", "null"]
        },
        "viewNegativeReactionTotals": {
            "type": ["string", "null"]
        },
        "viewReactionRatios": {
            "type": ["string", "null"]
        },
        "viewNegativeReactionRatios": {
            "type": ["string", "null"]
        },
        "addReaction": {
            "type": ["string", "null"]
        },
        "addNegativeReaction": {
            "type": ["string", "null"]
        },
        "overrideReaction": {
            "type": ["string", "null"]
        },
        "overrideCommentReaction": {
            "type": ["string", "null"]
        },
    },
    "additionalProperties": False
}

PRIVATE_MEDIA_FILE_OPERATIONS_SCHEMA: Any = {
    "type": "object",
    "properties": {
        "view": {
            "type": ["string", "null"]
        },
    },
    "additionalProperties": False
}

PROFILE_OPERATIONS_SCHEMA: Any = {
    "type": "object",
    "properties": {
        "edit": {
            "type": ["string", "null"]
        },
        "viewEmail": {
            "type": ["string", "null"]
        },
    },
    "additionalProperties": False
}

REACTION_OPERATIONS_SCHEMA: Any = {
    "type": "object",
    "properties": {
        "view": {
            "type": ["string", "null"]
        },
        "delete": {
            "type": ["string", "null"]
        },
    },
    "additionalProperties": False
}

STORY_OPERATIONS_SCHEMA: Any = {
    "type": "object",
    "properties": {
        "edit": {
            "type": ["string", "null"]
        },
        "delete": {
            "type": ["string", "null"]
        },
    },
    "additionalProperties": False
}

SUBSCRIBER_OPERATIONS_SCHEMA: Any = {
    "type": "object",
    "properties": {
        "view": {
            "type": ["string", "null"]
        },
        "delete": {
            "type": ["string", "null"]
        },
    },
    "additionalProperties": False
}

SUBSCRIPTION_OPERATIONS_SCHEMA: Any = {
    "type": "object",
    "properties": {
        "view": {
            "type": ["string", "null"]
        },
        "delete": {
            "type": ["string", "null"]
        },
    },
    "additionalProperties": False
}

ACCEPTED_REACTIONS_SCHEMA: Any = {
    "type": "object",
    "properties": {
        "positive": {
            "type": "string"
        },
        "negative": {
            "type": "string"
        },
    },
    "required": [
        "positive",
        "negative",
    ],
    "additionalProperties": False
}

ASYNC_OPERATION_CREATED_SCHEMA: Any = {
    "type": "object",
    "properties": {
        "id": {
            "type": "string"
        },
    },
    "required": [
        "id",
    ],
    "additionalProperties": False
}

AVATAR_IMAGE_SCHEMA: Any = {
    "type": "object",
    "properties": {
        "mediaId": {
            "type": "string"
        },
        "path": {
            "type": "string"
        },
        "width": {
            "type": ["integer", "null"]
        },
        "height": {
            "type": ["integer", "null"]
        },
        "shape": {
            "type": ["string", "null"]
        },
    },
    "required": [
        "mediaId",
        "path",
    ],
    "additionalProperties": False
}

AVATAR_INFO_SCHEMA: Any = {
    "type": "object",
    "properties": {
        "id": {
            "type": "string"
        },
        "mediaId": {
            "type": "string"
        },
        "path": {
            "type": "string"
        },
        "width": {
            "type": ["integer", "null"]
        },
        "height": {
            "type": ["integer", "null"]
        },
        "shape": {
            "type": ["string", "null"]
        },
        "ordinal": {
            "type": "integer"
        },
    },
    "required": [
        "id",
        "mediaId",
        "path",
        "ordinal",
    ],
    "additionalProperties": False
}

AVATAR_INFO_ARRAY_SCHEMA = array_schema(AVATAR_INFO_SCHEMA)

AVATAR_ORDINAL_SCHEMA: Any = {
    "type": "object",
    "properties": {
        "id": {
            "type": "string"
        },
        "ordinal": {
            "type": "integer"
        },
    },
    "required": [
        "id",
        "ordinal",
    ],
    "additionalProperties": False
}

AVATAR_ORDINAL_ARRAY_SCHEMA = array_schema(AVATAR_ORDINAL_SCHEMA)

BLOCKED_INSTANT_INFO_SCHEMA: Any = {
    "type": "object",
    "properties": {
        "id": {
            "type": "string"
        },
        "storyType": {
            "type": "string"
        },
        "entryId": {
            "type": ["string", "null"]
        },
        "remoteNodeName": {
            "type": ["string", "null"]
        },
        "remotePostingId": {
            "type": ["string", "null"]
        },
        "remoteOwnerName": {
            "type": ["string", "null"]
        },
        "createdAt": {
            "type": "integer"
        },
        "deadline": {
            "type": ["integer", "null"]
        },
    },
    "required": [
        "id",
        "storyType",
        "createdAt",
    ],
    "additionalProperties": False
}

BLOCKED_INSTANT_INFO_ARRAY_SCHEMA = array_schema(BLOCKED_INSTANT_INFO_SCHEMA)

BLOCKED_POSTING_INSTANT_INFO_SCHEMA: Any = {
    "type": "object",
    "properties": {
        "id": {
            "type": "string"
        },
        "storyType": {
            "type": "string"
        },
        "remoteOwnerName": {
            "type": ["string", "null"]
        },
        "deadline": {
            "type": ["integer", "null"]
        },
    },
    "required": [
        "id",
        "storyType",
    ],
    "additionalProperties": False
}

BLOCKED_USERS_CHECKSUMS_SCHEMA: Any = {
    "type": "object",
    "properties": {
        "visibility": {
            "type": "integer"
        },
    },
    "required": [
        "visibility",
    ],
    "additionalProperties": False
}

CARTE_INFO_SCHEMA: Any = {
    "type": "object",
    "properties": {
        "carte": {
            "type": "string"
        },
        "beginning": {
            "type": "integer"
        },
        "deadline": {
            "type": "integer"
        },
        "permissions": {
            "type": ["array", "null"],
            "items": {
                "type": "string"
            }
        },
    },
    "required": [
        "carte",
        "beginning",
        "deadline",
    ],
    "additionalProperties": False
}

CARTE_SET_SCHEMA: Any = {
    "type": "object",
    "properties": {
        "cartesIp": {
            "type": ["string", "null"]
        },
        "cartes": {
            "type": "array",
            "items": CARTE_INFO_SCHEMA
        },
        "createdAt": {
            "type": "integer"
        },
    },
    "required": [
        "cartes",
        "createdAt",
    ],
    "additionalProperties": False
}

CLIENT_REACTION_INFO_SCHEMA: Any = {
    "type": "object",
    "properties": {
        "negative": {
            "type": "boolean"
        },
        "emoji": {
            "type": "integer"
        },
        "createdAt": {
            "type": "integer"
        },
        "deadline": {
            "type": ["integer", "null"]
        },
    },
    "required": [
        "negative",
        "emoji",
        "createdAt",
    ],
    "additionalProperties": False
}

COMMENT_TOTAL_INFO_SCHEMA: Any = {
    "type": "object",
    "properties": {
        "total": {
            "type": "integer"
        },
    },
    "required": [
        "total",
    ],
    "additionalProperties": False
}

CONTACT_INFO_SCHEMA: Any = {
    "type": "object",
    "properties": {
        "nodeName": {
            "type": "string"
        },
        "fullName": {
            "type": ["string", "null"]
        },
        "gender": {
            "type": ["string", "null"]
        },
        "avatar": to_nullable_object_schema(AVATAR_IMAGE_SCHEMA),
        "closeness": {
            "type": "number"
        },
        "hasFeedSubscriber": {
            "type": ["boolean", "null"]
        },
        "hasFeedSubscription": {
            "type": ["boolean", "null"]
        },
        "hasFriend": {
            "type": ["boolean", "null"]
        },
        "hasFriendOf": {
            "type": ["boolean", "null"]
        },
        "hasBlock": {
            "type": ["boolean", "null"]
        },
        "hasBlockBy": {
            "type": ["boolean", "null"]
        },
        "operations": to_nullable_object_schema(CONTACT_OPERATIONS_SCHEMA),
        "ownerOperations": to_nullable_object_schema(CONTACT_OPERATIONS_SCHEMA),
        "adminOperations": to_nullable_object_schema(CONTACT_OPERATIONS_SCHEMA),
    },
    "required": [
        "nodeName",
        "closeness",
    ],
    "additionalProperties": False
}

CONTACT_INFO_ARRAY_SCHEMA = array_schema(CONTACT_INFO_SCHEMA)

CREDENTIALS_CREATED_SCHEMA: Any = {
    "type": "object",
    "properties": {
        "created": {
            "type": "boolean"
        },
    },
    "required": [
        "created",
    ],
    "additionalProperties": False
}

DOMAIN_AVAILABLE_SCHEMA: Any = {
    "type": "object",
    "properties": {
        "name": {
            "type": "string"
        },
    },
    "required": [
        "name",
    ],
    "additionalProperties": False
}

DOMAIN_INFO_SCHEMA: Any = {
    "type": "object",
    "properties": {
        "name": {
            "type": "string"
        },
        "nodeId": {
            "type": "string"
        },
        "createdAt": {
            "type": "integer"
        },
    },
    "required": [
        "name",
        "nodeId",
        "createdAt",
    ],
    "additionalProperties": False
}

DOMAIN_INFO_ARRAY_SCHEMA = array_schema(DOMAIN_INFO_SCHEMA)

EMAIL_HINT_SCHEMA: Any = {
    "type": "object",
    "properties": {
        "emailHint": {
            "type": "string"
        },
    },
    "required": [
        "emailHint",
    ],
    "additionalProperties": False
}

FEED_REFERENCE_SCHEMA: Any = {
    "type": "object",
    "properties": {
        "feedName": {
            "type": "string"
        },
        "publishedAt": {
            "type": "integer"
        },
        "pinned": {
            "type": ["boolean", "null"]
        },
        "moment": {
            "type": "integer"
        },
        "storyId": {
            "type": "string"
        },
        "operations": to_nullable_object_schema(STORY_OPERATIONS_SCHEMA),
    },
    "required": [
        "feedName",
        "publishedAt",
        "moment",
        "storyId",
    ],
    "additionalProperties": False
}

FEED_STATUS_SCHEMA: Any = {
    "type": "object",
    "properties": {
        "total": {
            "type": "integer"
        },
        "totalPinned": {
            "type": "integer"
        },
        "lastMoment": {
            "type": ["integer", "null"]
        },
        "notViewed": {
            "type": ["integer", "null"]
        },
        "notRead": {
            "type": ["integer", "null"]
        },
        "notViewedMoment": {
            "type": ["integer", "null"]
        },
        "notReadMoment": {
            "type": ["integer", "null"]
        },
    },
    "required": [
        "total",
        "totalPinned",
    ],
    "additionalProperties": False
}

FEED_WITH_STATUS_SCHEMA: Any = {
    "type": "object",
    "properties": {
        "feedName": {
            "type": "string"
        },
        "notViewed": {
            "type": "integer"
        },
        "notRead": {
            "type": "integer"
        },
    },
    "required": [
        "feedName",
        "notViewed",
        "notRead",
    ],
    "additionalProperties": False
}

FRIEND_GROUP_DETAILS_SCHEMA: Any = {
    "type": "object",
    "properties": {
        "id": {
            "type": "string"
        },
        "title": {
            "type": ["string", "null"]
        },
        "addedAt": {
            "type": "integer"
        },
        "operations": to_nullable_object_schema(FRIEND_OPERATIONS_SCHEMA),
    },
    "required": [
        "id",
        "addedAt",
    ],
    "additionalProperties": False
}

FRIEND_GROUP_INFO_SCHEMA: Any = {
    "type": "object",
    "properties": {
        "id": {
            "type": "string"
        },
        "title": {
            "type": ["string", "null"]
        },
        "createdAt": {
            "type": "integer"
        },
        "operations": to_nullable_object_schema(FRIEND_GROUP_OPERATIONS_SCHEMA),
    },
    "required": [
        "id",
        "createdAt",
    ],
    "additionalProperties": False
}

FRIEND_GROUP_INFO_ARRAY_SCHEMA = array_schema(FRIEND_GROUP_INFO_SCHEMA)

FRIEND_GROUPS_FEATURES_SCHEMA: Any = {
    "type": "object",
    "properties": {
        "available": {
            "type": "array",
            "items": FRIEND_GROUP_INFO_SCHEMA
        },
        "memberOf": {
            "type": ["array", "null"],
            "items": FRIEND_GROUP_DETAILS_SCHEMA
        },
    },
    "required": [
        "available",
    ],
    "additionalProperties": False
}

FRIEND_INFO_SCHEMA: Any = {
    "type": "object",
    "properties": {
        "nodeName": {
            "type": "string"
        },
        "contact": to_nullable_object_schema(CONTACT_INFO_SCHEMA),
        "groups": {
            "type": ["array", "null"],
            "items": FRIEND_GROUP_DETAILS_SCHEMA
        },
    },
    "required": [
        "nodeName",
    ],
    "additionalProperties": False
}

FRIEND_INFO_ARRAY_SCHEMA = array_schema(FRIEND_INFO_SCHEMA)

FRIEND_OF_INFO_SCHEMA: Any = {
    "type": "object",
    "properties": {
        "remoteNodeName": {
            "type": "string"
        },
        "contact": to_nullable_object_schema(CONTACT_INFO_SCHEMA),
        "groups": {
            "type": ["array", "null"],
            "items": FRIEND_GROUP_DETAILS_SCHEMA
        },
    },
    "required": [
        "remoteNodeName",
    ],
    "additionalProperties": False
}

FRIEND_OF_INFO_ARRAY_SCHEMA = array_schema(FRIEND_OF_INFO_SCHEMA)

FUNDRAISER_INFO_SCHEMA: Any = {
    "type": "object",
    "properties": {
        "title": {
            "type": "string"
        },
        "qrCode": {
            "type": ["string", "null"]
        },
        "text": {
            "type": ["string", "null"]
        },
        "href": {
            "type": ["string", "null"]
        },
    },
    "required": [
        "title",
    ],
    "additionalProperties": False
}

LINK_PREVIEW_SCHEMA: Any = {
    "type": "object",
    "properties": {
        "siteName": {
            "type": ["string", "null"]
        },
        "url": {
            "type": ["string", "null"]
        },
        "title": {
            "type": ["string", "null"]
        },
        "description": {
            "type": ["string", "null"]
        },
        "imageHash": {
            "type": ["string", "null"]
        },
    },
    "additionalProperties": False
}

LINK_PREVIEW_INFO_SCHEMA: Any = {
    "type": "object",
    "properties": {
        "siteName": {
            "type": ["string", "null"]
        },
        "url": {
            "type": ["string", "null"]
        },
        "title": {
            "type": ["string", "null"]
        },
        "description": {
            "type": ["string", "null"]
        },
        "imageUrl": {
            "type": ["string", "null"]
        },
    },
    "additionalProperties": False
}

MEDIA_FILE_PREVIEW_INFO_SCHEMA: Any = {
    "type": "object",
    "properties": {
        "targetWidth": {
            "type": "integer"
        },
        "width": {
            "type": "integer"
        },
        "height": {
            "type": "integer"
        },
        "original": {
            "type": ["boolean", "null"]
        },
    },
    "required": [
        "targetWidth",
        "width",
        "height",
    ],
    "additionalProperties": False
}

NODE_NAME_INFO_SCHEMA: Any = {
    "type": "object",
    "properties": {
        "name": {
            "type": ["string", "null"]
        },
        "operationStatus": {
            "type": ["string", "null"]
        },
        "operationStatusUpdated": {
            "type": ["integer", "null"]
        },
        "operationErrorCode": {
            "type": ["string", "null"]
        },
        "operationErrorMessage": {
            "type": ["string", "null"]
        },
        "operations": to_nullable_object_schema(NODE_NAME_OPERATIONS_SCHEMA),
    },
    "additionalProperties": False
}

PEOPLE_GENERAL_INFO_SCHEMA: Any = {
    "type": "object",
    "properties": {
        "feedSubscribersTotal": {
            "type": ["integer", "null"]
        },
        "feedSubscriptionsTotal": {
            "type": ["integer", "null"]
        },
        "friendsTotal": {
            "type": ["object", "null"],
            "patternProperties": {
                "^.*$": {
                    "type": "integer"
                }
            }
        },
        "friendOfsTotal": {
            "type": ["integer", "null"]
        },
        "blockedTotal": {
            "type": ["integer", "null"]
        },
        "blockedByTotal": {
            "type": ["integer", "null"]
        },
        "operations": to_nullable_object_schema(PEOPLE_OPERATIONS_SCHEMA),
    },
    "additionalProperties": False
}

POSTING_FEATURES_SCHEMA: Any = {
    "type": "object",
    "properties": {
        "post": {
            "type": ["boolean", "null"]
        },
        "subjectPresent": {
            "type": "boolean"
        },
        "sourceFormats": {
            "type": "array",
            "items": {
                "type": "string"
            }
        },
        "mediaMaxSize": {
            "type": "integer"
        },
        "imageRecommendedSize": {
            "type": "integer"
        },
        "imageRecommendedPixels": {
            "type": "integer"
        },
        "imageFormats": {
            "type": "array",
            "items": {
                "type": "string"
            }
        },
    },
    "required": [
        "subjectPresent",
        "sourceFormats",
        "mediaMaxSize",
        "imageRecommendedSize",
        "imageRecommendedPixels",
        "imageFormats",
    ],
    "additionalProperties": False
}

POSTING_SOURCE_INFO_SCHEMA: Any = {
    "type": "object",
    "properties": {
        "nodeName": {
            "type": "string"
        },
        "fullName": {
            "type": ["string", "null"]
        },
        "avatar": to_nullable_object_schema(AVATAR_IMAGE_SCHEMA),
        "feedName": {
            "type": "string"
        },
        "postingId": {
            "type": "string"
        },
        "createdAt": {
            "type": "integer"
        },
    },
    "required": [
        "nodeName",
        "feedName",
        "postingId",
        "createdAt",
    ],
    "additionalProperties": False
}

PRIVATE_MEDIA_FILE_INFO_SCHEMA: Any = {
    "type": "object",
    "properties": {
        "id": {
            "type": "string"
        },
        "hash": {
            "type": "string"
        },
        "path": {
            "type": "string"
        },
        "mimeType": {
            "type": "string"
        },
        "width": {
            "type": ["integer", "null"]
        },
        "height": {
            "type": ["integer", "null"]
        },
        "orientation": {
            "type": ["integer", "null"]
        },
        "size": {
            "type": "integer"
        },
        "postingId": {
            "type": ["string", "null"]
        },
        "previews": {
            "type": ["array", "null"],
            "items": MEDIA_FILE_PREVIEW_INFO_SCHEMA
        },
        "operations": to_nullable_object_schema(PRIVATE_MEDIA_FILE_OPERATIONS_SCHEMA),
    },
    "required": [
        "id",
        "hash",
        "path",
        "mimeType",
        "size",
    ],
    "additionalProperties": False
}

PROFILE_INFO_SCHEMA: Any = {
    "type": "object",
    "properties": {
        "fullName": {
            "type": ["string", "null"]
        },
        "gender": {
            "type": ["string", "null"]
        },
        "email": {
            "type": ["string", "null"]
        },
        "title": {
            "type": ["string", "null"]
        },
        "bioSrc": {
            "type": ["string", "null"]
        },
        "bioSrcFormat": {
            "type": ["string", "null"]
        },
        "bioHtml": {
            "type": ["string", "null"]
        },
        "avatar": to_nullable_object_schema(AVATAR_INFO_SCHEMA),
        "fundraisers": {
            "type": ["array", "null"],
            "items": FUNDRAISER_INFO_SCHEMA
        },
        "operations": to_nullable_object_schema(PROFILE_OPERATIONS_SCHEMA),
    },
    "additionalProperties": False
}

PUBLIC_MEDIA_FILE_INFO_SCHEMA: Any = {
    "type": "object",
    "properties": {
        "id": {
            "type": "string"
        },
        "path": {
            "type": "string"
        },
        "width": {
            "type": ["integer", "null"]
        },
        "height": {
            "type": ["integer", "null"]
        },
        "orientation": {
            "type": ["integer", "null"]
        },
        "size": {
            "type": "integer"
        },
    },
    "required": [
        "id",
        "path",
        "size",
    ],
    "additionalProperties": False
}

REACTION_INFO_SCHEMA: Any = {
    "type": "object",
    "properties": {
        "ownerName": {
            "type": ["string", "null"]
        },
        "ownerFullName": {
            "type": ["string", "null"]
        },
        "ownerGender": {
            "type": ["string", "null"]
        },
        "ownerAvatar": to_nullable_object_schema(AVATAR_IMAGE_SCHEMA),
        "postingId": {
            "type": ["string", "null"]
        },
        "postingRevisionId": {
            "type": ["string", "null"]
        },
        "commentId": {
            "type": ["string", "null"]
        },
        "commentRevisionId": {
            "type": ["string", "null"]
        },
        "negative": {
            "type": ["boolean", "null"]
        },
        "emoji": {
            "type": ["integer", "null"]
        },
        "moment": {
            "type": ["integer", "null"]
        },
        "createdAt": {
            "type": ["integer", "null"]
        },
        "deadline": {
            "type": ["integer", "null"]
        },
        "signature": {
            "type": ["string", "null"]
        },
        "signatureVersion": {
            "type": ["integer", "null"]
        },
        "operations": to_nullable_object_schema(REACTION_OPERATIONS_SCHEMA),
        "ownerOperations": to_nullable_object_schema(REACTION_OPERATIONS_SCHEMA),
        "seniorOperations": to_nullable_object_schema(REACTION_OPERATIONS_SCHEMA),
        "majorOperations": to_nullable_object_schema(REACTION_OPERATIONS_SCHEMA),
    },
    "additionalProperties": False
}

REACTION_INFO_ARRAY_SCHEMA = array_schema(REACTION_INFO_SCHEMA)

REACTIONS_SLICE_INFO_SCHEMA: Any = {
    "type": "object",
    "properties": {
        "before": {
            "type": "integer"
        },
        "after": {
            "type": "integer"
        },
        "total": {
            "type": "integer"
        },
        "reactions": {
            "type": "array",
            "items": REACTION_INFO_SCHEMA
        },
    },
    "required": [
        "before",
        "after",
        "total",
        "reactions",
    ],
    "additionalProperties": False
}

REACTION_TOTAL_INFO_SCHEMA: Any = {
    "type": "object",
    "properties": {
        "emoji": {
            "type": "integer"
        },
        "total": {
            "type": ["integer", "null"]
        },
        "share": {
            "type": ["number", "null"],
            "minimum": 0,
            "maximum": 1
        },
    },
    "required": [
        "emoji",
    ],
    "additionalProperties": False
}

REACTION_TOTALS_INFO_SCHEMA: Any = {
    "type": "object",
    "properties": {
        "entryId": {
            "type": "string"
        },
        "positive": {
            "type": ["array", "null"],
            "items": REACTION_TOTAL_INFO_SCHEMA
        },
        "negative": {
            "type": ["array", "null"],
            "items": REACTION_TOTAL_INFO_SCHEMA
        },
    },
    "required": [
        "entryId",
    ],
    "additionalProperties": False
}

REACTION_TOTALS_INFO_ARRAY_SCHEMA = array_schema(REACTION_TOTALS_INFO_SCHEMA)

REGISTERED_NAME_SECRET_SCHEMA: Any = {
    "type": "object",
    "properties": {
        "name": {
            "type": "string"
        },
        "mnemonic": {
            "type": ["array", "null"],
            "items": {
                "type": "string"
            },
            "minItems": 24,
            "maxItems": 24
        },
        "secret": {
            "type": ["string", "null"]
        },
    },
    "required": [
        "name",
    ],
    "additionalProperties": False
}

REMOTE_MEDIA_INFO_SCHEMA: Any = {
    "type": "object",
    "properties": {
        "id": {
            "type": "string"
        },
        "hash": {
            "type": ["string", "null"]
        },
        "digest": {
            "type": ["string", "null"]
        },
    },
    "required": [
        "id",
    ],
    "additionalProperties": False
}

REMOTE_POSTING_VERIFICATION_INFO_SCHEMA: Any = {
    "type": "object",
    "properties": {
        "id": {
            "type": "string"
        },
        "nodeName": {
            "type": "string"
        },
        "postingId": {
            "type": "string"
        },
        "revisionId": {
            "type": ["string", "null"]
        },
        "status": {
            "type": ["string", "null"]
        },
        "errorCode": {
            "type": ["string", "null"]
        },
        "errorMessage": {
            "type": ["string", "null"]
        },
    },
    "required": [
        "id",
        "nodeName",
        "postingId",
    ],
    "additionalProperties": False
}

REMOTE_REACTION_VERIFICATION_INFO_SCHEMA: Any = {
    "type": "object",
    "properties": {
        "id": {
            "type": "string"
        },
        "nodeName": {
            "type": "string"
        },
        "postingId": {
            "type": "string"
        },
        "reactionOwnerName": {
            "type": "string"
        },
        "status": {
            "type": ["string", "null"]
        },
        "errorCode": {
            "type": ["string", "null"]
        },
        "errorMessage": {
            "type": ["string", "null"]
        },
    },
    "required": [
        "id",
        "nodeName",
        "postingId",
        "reactionOwnerName",
    ],
    "additionalProperties": False
}

REPLIED_TO_SCHEMA: Any = {
    "type": "object",
    "properties": {
        "id": {
            "type": "string"
        },
        "revisionId": {
            "type": ["string", "null"]
        },
        "name": {
            "type": "string"
        },
        "fullName": {
            "type": ["string", "null"]
        },
        "gender": {
            "type": ["string", "null"]
        },
        "avatar": to_nullable_object_schema(AVATAR_IMAGE_SCHEMA),
        "heading": {
            "type": ["string", "null"]
        },
        "digest": {
            "type": "string"
        },
    },
    "required": [
        "id",
        "name",
        "digest",
    ],
    "additionalProperties": False
}

RESULT_SCHEMA: Any = {
    "type": "object",
    "properties": {
        "errorCode": {
            "type": "string"
        },
        "message": {
            "type": ["string", "null"]
        },
    },
    "required": [
        "errorCode",
    ],
    "additionalProperties": False
}

SHERIFF_MARK_SCHEMA: Any = {
    "type": "object",
    "properties": {
        "sheriffName": {
            "type": "string"
        },
    },
    "required": [
        "sheriffName",
    ],
    "additionalProperties": False
}

SETTING_INFO_SCHEMA: Any = {
    "type": "object",
    "properties": {
        "name": {
            "type": "string"
        },
        "value": {
            "type": ["string", "null"]
        },
    },
    "required": [
        "name",
    ],
    "additionalProperties": False
}

SETTING_INFO_ARRAY_SCHEMA = array_schema(SETTING_INFO_SCHEMA)

SETTING_TYPE_MODIFIERS_SCHEMA: Any = {
    "type": "object",
    "properties": {
        "format": {
            "type": ["string", "null"]
        },
        "min": {
            "type": ["string", "null"]
        },
        "max": {
            "type": ["string", "null"]
        },
        "multiline": {
            "type": ["boolean", "null"]
        },
        "never": {
            "type": ["boolean", "null"]
        },
        "always": {
            "type": ["boolean", "null"]
        },
        "principals": {
            "type": ["array", "null"],
            "items": {
                "type": "string"
            }
        },
    },
    "additionalProperties": False
}

SHERIFF_COMPLAIN_GROUP_INFO_SCHEMA: Any = {
    "type": "object",
    "properties": {
        "id": {
            "type": "string"
        },
        "remoteNodeName": {
            "type": "string"
        },
        "remoteNodeFullName": {
            "type": ["string", "null"]
        },
        "remoteFeedName": {
            "type": "string"
        },
        "remotePostingId": {
            "type": ["string", "null"]
        },
        "remotePostingRevisionId": {
            "type": ["string", "null"]
        },
        "remotePostingOwnerName": {
            "type": ["string", "null"]
        },
        "remotePostingOwnerFullName": {
            "type": ["string", "null"]
        },
        "remotePostingOwnerGender": {
            "type": ["string", "null"]
        },
        "remotePostingHeading": {
            "type": ["string", "null"]
        },
        "remoteCommentId": {
            "type": ["string", "null"]
        },
        "remoteCommentRevisionId": {
            "type": ["string", "null"]
        },
        "remoteCommentOwnerName": {
            "type": ["string", "null"]
        },
        "remoteCommentOwnerFullName": {
            "type": ["string", "null"]
        },
        "remoteCommentOwnerGender": {
            "type": ["string", "null"]
        },
        "remoteCommentHeading": {
            "type": ["string", "null"]
        },
        "createdAt": {
            "type": "integer"
        },
        "moment": {
            "type": "integer"
        },
        "status": {
            "type": "string"
        },
        "decisionCode": {
            "type": ["string", "null"]
        },
        "decisionDetails": {
            "type": ["string", "null"]
        },
        "decidedAt": {
            "type": ["integer", "null"]
        },
        "anonymous": {
            "type": ["boolean", "null"]
        },
    },
    "required": [
        "id",
        "remoteNodeName",
        "remoteFeedName",
        "createdAt",
        "moment",
        "status",
    ],
    "additionalProperties": False
}

SHERIFF_COMPLAIN_GROUPS_SLICE_INFO_SCHEMA: Any = {
    "type": "object",
    "properties": {
        "before": {
            "type": "integer"
        },
        "after": {
            "type": "integer"
        },
        "groups": {
            "type": "array",
            "items": SHERIFF_COMPLAIN_GROUP_INFO_SCHEMA
        },
        "total": {
            "type": "integer"
        },
        "totalInPast": {
            "type": "integer"
        },
        "totalInFuture": {
            "type": "integer"
        },
    },
    "required": [
        "before",
        "after",
        "groups",
        "total",
        "totalInPast",
        "totalInFuture",
    ],
    "additionalProperties": False
}

SHERIFF_COMPLAIN_INFO_SCHEMA: Any = {
    "type": "object",
    "properties": {
        "id": {
            "type": "string"
        },
        "ownerName": {
            "type": "string"
        },
        "ownerFullName": {
            "type": ["string", "null"]
        },
        "ownerGender": {
            "type": ["string", "null"]
        },
        "group": to_nullable_object_schema(SHERIFF_COMPLAIN_GROUP_INFO_SCHEMA),
        "reasonCode": {
            "type": "string"
        },
        "reasonDetails": {
            "type": ["string", "null"]
        },
        "anonymousRequested": {
            "type": ["boolean", "null"]
        },
        "createdAt": {
            "type": "integer"
        },
    },
    "required": [
        "id",
        "ownerName",
        "reasonCode",
        "createdAt",
    ],
    "additionalProperties": False
}

SHERIFF_COMPLAIN_INFO_ARRAY_SCHEMA = array_schema(SHERIFF_COMPLAIN_INFO_SCHEMA)

SHERIFF_ORDER_INFO_SCHEMA: Any = {
    "type": "object",
    "properties": {
        "id": {
            "type": "string"
        },
        "delete": {
            "type": ["boolean", "null"]
        },
        "sheriffName": {
            "type": "string"
        },
        "nodeName": {
            "type": "string"
        },
        "nodeFullName": {
            "type": ["string", "null"]
        },
        "feedName": {
            "type": "string"
        },
        "postingId": {
            "type": ["string", "null"]
        },
        "postingRevisionId": {
            "type": ["string", "null"]
        },
        "postingOwnerName": {
            "type": ["string", "null"]
        },
        "postingOwnerFullName": {
            "type": ["string", "null"]
        },
        "postingOwnerGender": {
            "type": ["string", "null"]
        },
        "postingHeading": {
            "type": ["string", "null"]
        },
        "commentId": {
            "type": ["string", "null"]
        },
        "commentRevisionId": {
            "type": ["string", "null"]
        },
        "commentOwnerName": {
            "type": ["string", "null"]
        },
        "commentOwnerFullName": {
            "type": ["string", "null"]
        },
        "commentOwnerGender": {
            "type": ["string", "null"]
        },
        "commentHeading": {
            "type": ["string", "null"]
        },
        "category": {
            "type": "string"
        },
        "reasonCode": {
            "type": ["string", "null"]
        },
        "reasonDetails": {
            "type": ["string", "null"]
        },
        "createdAt": {
            "type": "integer"
        },
        "signature": {
            "type": "string"
        },
        "signatureVersion": {
            "type": "integer"
        },
        "complainGroupId": {
            "type": ["string", "null"]
        },
    },
    "required": [
        "id",
        "sheriffName",
        "nodeName",
        "feedName",
        "category",
        "createdAt",
        "signature",
        "signatureVersion",
    ],
    "additionalProperties": False
}

STORY_SUMMARY_BLOCKED_SCHEMA: Any = {
    "type": "object",
    "properties": {
        "operations": {
            "type": "array",
            "items": {
                "type": "string"
            }
        },
        "period": {
            "type": ["integer", "null"]
        },
    },
    "required": [
        "operations",
    ],
    "additionalProperties": False
}

STORY_SUMMARY_FRIEND_GROUP_SCHEMA: Any = {
    "type": "object",
    "properties": {
        "id": {
            "type": ["string", "null"]
        },
        "title": {
            "type": ["string", "null"]
        },
    },
    "additionalProperties": False
}

STORY_SUMMARY_ENTRY_SCHEMA: Any = {
    "type": "object",
    "properties": {
        "ownerName": {
            "type": ["string", "null"]
        },
        "ownerFullName": {
            "type": ["string", "null"]
        },
        "ownerGender": {
            "type": ["string", "null"]
        },
        "heading": {
            "type": ["string", "null"]
        },
        "sheriffs": {
            "type": ["array", "null"],
            "items": {
                "type": "string"
            }
        },
        "sheriffMarks": {
            "type": ["array", "null"],
            "items": SHERIFF_MARK_SCHEMA
        },
    },
    "additionalProperties": False
}

STORY_SUMMARY_NODE_SCHEMA: Any = {
    "type": "object",
    "properties": {
        "ownerName": {
            "type": ["string", "null"]
        },
        "ownerFullName": {
            "type": ["string", "null"]
        },
        "ownerGender": {
            "type": ["string", "null"]
        },
    },
    "additionalProperties": False
}

STORY_SUMMARY_REACTION_SCHEMA: Any = {
    "type": "object",
    "properties": {
        "ownerName": {
            "type": ["string", "null"]
        },
        "ownerFullName": {
            "type": ["string", "null"]
        },
        "ownerGender": {
            "type": ["string", "null"]
        },
        "emoji": {
            "type": ["integer", "null"]
        },
    },
    "additionalProperties": False
}

STORY_SUMMARY_SHERIFF_SCHEMA: Any = {
    "type": "object",
    "properties": {
        "sheriffName": {
            "type": "string"
        },
        "orderId": {
            "type": ["string", "null"]
        },
        "complainId": {
            "type": ["string", "null"]
        },
    },
    "required": [
        "sheriffName",
    ],
    "additionalProperties": False
}

SUBSCRIBER_INFO_SCHEMA: Any = {
    "type": "object",
    "properties": {
        "id": {
            "type": "string"
        },
        "type": {
            "type": "string"
        },
        "feedName": {
            "type": ["string", "null"]
        },
        "postingId": {
            "type": ["string", "null"]
        },
        "nodeName": {
            "type": "string"
        },
        "contact": to_nullable_object_schema(CONTACT_INFO_SCHEMA),
        "createdAt": {
            "type": "integer"
        },
        "operations": to_nullable_object_schema(SUBSCRIBER_OPERATIONS_SCHEMA),
        "ownerOperations": to_nullable_object_schema(SUBSCRIBER_OPERATIONS_SCHEMA),
        "adminOperations": to_nullable_object_schema(SUBSCRIBER_OPERATIONS_SCHEMA),
    },
    "required": [
        "id",
        "type",
        "nodeName",
        "createdAt",
    ],
    "additionalProperties": False
}

SUBSCRIBER_INFO_ARRAY_SCHEMA = array_schema(SUBSCRIBER_INFO_SCHEMA)

SUBSCRIPTION_INFO_SCHEMA: Any = {
    "type": "object",
    "properties": {
        "id": {
            "type": "string"
        },
        "type": {
            "type": "string"
        },
        "feedName": {
            "type": ["string", "null"]
        },
        "remoteNodeName": {
            "type": "string"
        },
        "contact": to_nullable_object_schema(CONTACT_INFO_SCHEMA),
        "remoteFeedName": {
            "type": ["string", "null"]
        },
        "remotePostingId": {
            "type": ["string", "null"]
        },
        "createdAt": {
            "type": "integer"
        },
        "reason": {
            "type": "string"
        },
        "operations": to_nullable_object_schema(SUBSCRIPTION_OPERATIONS_SCHEMA),
    },
    "required": [
        "id",
        "type",
        "remoteNodeName",
        "createdAt",
        "reason",
    ],
    "additionalProperties": False
}

SUBSCRIPTION_INFO_ARRAY_SCHEMA = array_schema(SUBSCRIPTION_INFO_SCHEMA)

TOKEN_INFO_SCHEMA: Any = {
    "type": "object",
    "properties": {
        "id": {
            "type": "string"
        },
        "token": {
            "type": "string"
        },
        "name": {
            "type": ["string", "null"]
        },
        "permissions": {
            "type": ["array", "null"],
            "items": {
                "type": "string"
            }
        },
        "pluginName": {
            "type": ["string", "null"]
        },
        "createdAt": {
            "type": "integer"
        },
        "deadline": {
            "type": ["integer", "null"]
        },
        "lastUsedAt": {
            "type": ["integer", "null"]
        },
        "lastUsedBrowser": {
            "type": ["string", "null"]
        },
        "lastUsedIp": {
            "type": ["string", "null"]
        },
    },
    "required": [
        "id",
        "token",
        "createdAt",
    ],
    "additionalProperties": False
}

TOKEN_INFO_ARRAY_SCHEMA = array_schema(TOKEN_INFO_SCHEMA)

UPDATE_INFO_SCHEMA: Any = {
    "type": "object",
    "properties": {
        "important": {
            "type": ["boolean", "null"]
        },
        "description": {
            "type": ["string", "null"]
        },
    },
    "additionalProperties": False
}

USER_LIST_INFO_SCHEMA: Any = {
    "type": "object",
    "properties": {
        "name": {
            "type": "string"
        },
        "total": {
            "type": "integer"
        },
    },
    "required": [
        "name",
        "total",
    ],
    "additionalProperties": False
}

USER_LIST_ITEM_INFO_SCHEMA: Any = {
    "type": "object",
    "properties": {
        "nodeName": {
            "type": "string"
        },
        "createdAt": {
            "type": "integer"
        },
        "moment": {
            "type": "integer"
        },
    },
    "required": [
        "nodeName",
        "createdAt",
        "moment",
    ],
    "additionalProperties": False
}

USER_LIST_SLICE_INFO_SCHEMA: Any = {
    "type": "object",
    "properties": {
        "listName": {
            "type": "string"
        },
        "before": {
            "type": "integer"
        },
        "after": {
            "type": "integer"
        },
        "items": {
            "type": "array",
            "items": USER_LIST_ITEM_INFO_SCHEMA
        },
        "total": {
            "type": "integer"
        },
        "totalInPast": {
            "type": "integer"
        },
        "totalInFuture": {
            "type": "integer"
        },
    },
    "required": [
        "listName",
        "before",
        "after",
        "items",
        "total",
        "totalInPast",
        "totalInFuture",
    ],
    "additionalProperties": False
}

WHO_AM_I_SCHEMA: Any = {
    "type": "object",
    "properties": {
        "nodeName": {
            "type": ["string", "null"]
        },
        "nodeNameChanging": {
            "type": ["boolean", "null"]
        },
        "fullName": {
            "type": ["string", "null"]
        },
        "gender": {
            "type": ["string", "null"]
        },
        "title": {
            "type": ["string", "null"]
        },
        "avatar": to_nullable_object_schema(AVATAR_IMAGE_SCHEMA),
    },
    "additionalProperties": False
}

ACTIVITY_REACTION_INFO_SCHEMA: Any = {
    "type": "object",
    "properties": {
        "remoteNodeName": {
            "type": "string"
        },
        "remoteFullName": {
            "type": ["string", "null"]
        },
        "remoteAvatar": to_nullable_object_schema(AVATAR_IMAGE_SCHEMA),
        "remotePostingId": {
            "type": "string"
        },
        "negative": {
            "type": "boolean"
        },
        "emoji": {
            "type": "integer"
        },
        "createdAt": {
            "type": "integer"
        },
    },
    "required": [
        "remoteNodeName",
        "remotePostingId",
        "negative",
        "emoji",
        "createdAt",
    ],
    "additionalProperties": False
}

ACTIVITY_REACTION_INFO_ARRAY_SCHEMA = array_schema(ACTIVITY_REACTION_INFO_SCHEMA)

BLOCKED_BY_USER_INFO_SCHEMA: Any = {
    "type": "object",
    "properties": {
        "id": {
            "type": "string"
        },
        "blockedOperation": {
            "type": "string"
        },
        "contact": to_nullable_object_schema(CONTACT_INFO_SCHEMA),
        "nodeName": {
            "type": "string"
        },
        "postingId": {
            "type": ["string", "null"]
        },
        "createdAt": {
            "type": "integer"
        },
        "deadline": {
            "type": ["integer", "null"]
        },
        "reason": {
            "type": ["string", "null"]
        },
    },
    "required": [
        "id",
        "blockedOperation",
        "nodeName",
        "createdAt",
    ],
    "additionalProperties": False
}

BLOCKED_BY_USER_INFO_ARRAY_SCHEMA = array_schema(BLOCKED_BY_USER_INFO_SCHEMA)

BLOCKED_USER_INFO_SCHEMA: Any = {
    "type": "object",
    "properties": {
        "id": {
            "type": "string"
        },
        "blockedOperation": {
            "type": "string"
        },
        "nodeName": {
            "type": "string"
        },
        "contact": to_nullable_object_schema(CONTACT_INFO_SCHEMA),
        "entryId": {
            "type": ["string", "null"]
        },
        "entryNodeName": {
            "type": ["string", "null"]
        },
        "entryPostingId": {
            "type": ["string", "null"]
        },
        "createdAt": {
            "type": "integer"
        },
        "deadline": {
            "type": ["integer", "null"]
        },
        "reasonSrc": {
            "type": ["string", "null"]
        },
        "reasonSrcFormat": {
            "type": ["string", "null"]
        },
        "reason": {
            "type": ["string", "null"]
        },
    },
    "required": [
        "id",
        "blockedOperation",
        "nodeName",
        "createdAt",
    ],
    "additionalProperties": False
}

BLOCKED_USER_INFO_ARRAY_SCHEMA = array_schema(BLOCKED_USER_INFO_SCHEMA)

BODY_SCHEMA: Any = {
    "type": "object",
    "properties": {
        "subject": {
            "type": ["string", "null"]
        },
        "text": {
            "type": ["string", "null"]
        },
        "linkPreviews": {
            "type": ["array", "null"],
            "items": LINK_PREVIEW_SCHEMA
        },
    },
    "additionalProperties": False
}

COMMENT_REVISION_INFO_SCHEMA: Any = {
    "type": "object",
    "properties": {
        "id": {
            "type": "string"
        },
        "postingRevisionId": {
            "type": "string"
        },
        "bodyPreview": {
            "type": ["string", "null"]
        },
        "bodySrcHash": {
            "type": "string"
        },
        "bodySrcFormat": {
            "type": ["string", "null"]
        },
        "body": {
            "type": "string"
        },
        "bodyFormat": {
            "type": ["string", "null"]
        },
        "heading": {
            "type": "string"
        },
        "createdAt": {
            "type": "integer"
        },
        "deletedAt": {
            "type": ["integer", "null"]
        },
        "deadline": {
            "type": ["integer", "null"]
        },
        "digest": {
            "type": "string"
        },
        "signature": {
            "type": ["string", "null"]
        },
        "signatureVersion": {
            "type": ["integer", "null"]
        },
        "clientReaction": to_nullable_object_schema(CLIENT_REACTION_INFO_SCHEMA),
        "reactions": to_nullable_object_schema(REACTION_TOTALS_INFO_SCHEMA),
    },
    "required": [
        "id",
        "postingRevisionId",
        "bodySrcHash",
        "body",
        "heading",
        "createdAt",
        "digest",
    ],
    "additionalProperties": False
}

COMMENT_REVISION_INFO_ARRAY_SCHEMA = array_schema(COMMENT_REVISION_INFO_SCHEMA)

FEATURES_SCHEMA: Any = {
    "type": "object",
    "properties": {
        "posting": POSTING_FEATURES_SCHEMA,
        "plugins": {
            "type": ["array", "null"],
            "items": {
                "type": "string"
            }
        },
        "feedWidth": {
            "type": "integer"
        },
        "friendGroups": to_nullable_object_schema(FRIEND_GROUPS_FEATURES_SCHEMA),
        "ask": {
            "type": ["array", "null"],
            "items": {
                "type": "string"
            }
        },
        "subscribed": {
            "type": ["boolean", "null"]
        },
    },
    "required": [
        "posting",
        "feedWidth",
    ],
    "additionalProperties": False
}

FEED_INFO_SCHEMA: Any = {
    "type": "object",
    "properties": {
        "feedName": {
            "type": "string"
        },
        "title": {
            "type": ["string", "null"]
        },
        "total": {
            "type": "integer"
        },
        "firstCreatedAt": {
            "type": ["integer", "null"]
        },
        "lastCreatedAt": {
            "type": ["integer", "null"]
        },
        "operations": to_nullable_object_schema(FEED_OPERATIONS_SCHEMA),
        "sheriffs": {
            "type": ["array", "null"],
            "items": {
                "type": "string"
            }
        },
        "sheriffMarks": {
            "type": ["array", "null"],
            "items": SHERIFF_MARK_SCHEMA
        },
    },
    "required": [
        "feedName",
        "total",
    ],
    "additionalProperties": False
}

FEED_INFO_ARRAY_SCHEMA = array_schema(FEED_INFO_SCHEMA)

MEDIA_ATTACHMENT_SCHEMA: Any = {
    "type": "object",
    "properties": {
        "media": to_nullable_object_schema(PRIVATE_MEDIA_FILE_INFO_SCHEMA),
        "remoteMedia": to_nullable_object_schema(REMOTE_MEDIA_INFO_SCHEMA),
        "embedded": {
            "type": "boolean"
        },
    },
    "required": [
        "embedded",
    ],
    "additionalProperties": False
}

POSTING_INFO_SCHEMA: Any = {
    "type": "object",
    "properties": {
        "id": {
            "type": "string"
        },
        "revisionId": {
            "type": "string"
        },
        "receiverRevisionId": {
            "type": ["string", "null"]
        },
        "totalRevisions": {
            "type": "integer"
        },
        "receiverName": {
            "type": ["string", "null"]
        },
        "receiverFullName": {
            "type": ["string", "null"]
        },
        "receiverGender": {
            "type": ["string", "null"]
        },
        "receiverAvatar": to_nullable_object_schema(AVATAR_IMAGE_SCHEMA),
        "receiverPostingId": {
            "type": ["string", "null"]
        },
        "parentMediaId": {
            "type": ["string", "null"]
        },
        "ownerName": {
            "type": "string"
        },
        "ownerFullName": {
            "type": ["string", "null"]
        },
        "ownerGender": {
            "type": ["string", "null"]
        },
        "ownerAvatar": to_nullable_object_schema(AVATAR_IMAGE_SCHEMA),
        "bodyPreview": {
            "type": ["string", "null"]
        },
        "bodySrc": {
            "type": ["string", "null"]
        },
        "bodySrcHash": {
            "type": "string"
        },
        "bodySrcFormat": {
            "type": ["string", "null"]
        },
        "body": {
            "type": "string"
        },
        "bodyFormat": {
            "type": ["string", "null"]
        },
        "media": {
            "type": ["array", "null"],
            "items": MEDIA_ATTACHMENT_SCHEMA
        },
        "heading": {
            "type": "string"
        },
        "updateInfo": to_nullable_object_schema(UPDATE_INFO_SCHEMA),
        "createdAt": {
            "type": "integer"
        },
        "editedAt": {
            "type": ["integer", "null"]
        },
        "deletedAt": {
            "type": ["integer", "null"]
        },
        "receiverCreatedAt": {
            "type": ["integer", "null"]
        },
        "receiverEditedAt": {
            "type": ["integer", "null"]
        },
        "receiverDeletedAt": {
            "type": ["integer", "null"]
        },
        "revisionCreatedAt": {
            "type": "integer"
        },
        "receiverRevisionCreatedAt": {
            "type": ["integer", "null"]
        },
        "deadline": {
            "type": ["integer", "null"]
        },
        "digest": {
            "type": "string"
        },
        "signature": {
            "type": ["string", "null"]
        },
        "signatureVersion": {
            "type": ["integer", "null"]
        },
        "feedReferences": {
            "type": ["array", "null"],
            "items": FEED_REFERENCE_SCHEMA
        },
        "blockedInstants": {
            "type": ["array", "null"],
            "items": BLOCKED_POSTING_INSTANT_INFO_SCHEMA
        },
        "operations": to_nullable_object_schema(POSTING_OPERATIONS_SCHEMA),
        "receiverOperations": to_nullable_object_schema(POSTING_OPERATIONS_SCHEMA),
        "commentOperations": to_nullable_object_schema(COMMENT_OPERATIONS_SCHEMA),
        "reactionOperations": to_nullable_object_schema(REACTION_OPERATIONS_SCHEMA),
        "commentReactionOperations": to_nullable_object_schema(REACTION_OPERATIONS_SCHEMA),
        "blockedOperations": {
            "type": ["array", "null"],
            "items": {
                "type": "string"
            }
        },
        "blockedCommentOperations": {
            "type": ["array", "null"],
            "items": {
                "type": "string"
            }
        },
        "sheriffs": {
            "type": ["array", "null"],
            "items": {
                "type": "string"
            }
        },
        "sheriffMarks": {
            "type": ["array", "null"],
            "items": SHERIFF_MARK_SCHEMA
        },
        "acceptedReactions": to_nullable_object_schema(ACCEPTED_REACTIONS_SCHEMA),
        "clientReaction": to_nullable_object_schema(CLIENT_REACTION_INFO_SCHEMA),
        "reactions": to_nullable_object_schema(REACTION_TOTALS_INFO_SCHEMA),
        "sources": {
            "type": ["array", "null"],
            "items": POSTING_SOURCE_INFO_SCHEMA
        },
        "totalComments": {
            "type": ["integer", "null"]
        },
    },
    "required": [
        "id",
        "revisionId",
        "totalRevisions",
        "ownerName",
        "bodySrcHash",
        "body",
        "heading",
        "createdAt",
        "revisionCreatedAt",
        "digest",
    ],
    "additionalProperties": False
}

POSTING_INFO_ARRAY_SCHEMA = array_schema(POSTING_INFO_SCHEMA)

POSTING_REVISION_INFO_SCHEMA: Any = {
    "type": "object",
    "properties": {
        "id": {
            "type": "string"
        },
        "receiverId": {
            "type": ["string", "null"]
        },
        "bodyPreview": {
            "type": ["string", "null"]
        },
        "bodySrcHash": {
            "type": "string"
        },
        "bodySrcFormat": {
            "type": ["string", "null"]
        },
        "body": {
            "type": "string"
        },
        "bodyFormat": {
            "type": ["string", "null"]
        },
        "media": {
            "type": ["array", "null"],
            "items": MEDIA_ATTACHMENT_SCHEMA
        },
        "heading": {
            "type": "string"
        },
        "updateInfo": to_nullable_object_schema(UPDATE_INFO_SCHEMA),
        "createdAt": {
            "type": "integer"
        },
        "deletedAt": {
            "type": ["integer", "null"]
        },
        "receiverCreatedAt": {
            "type": ["integer", "null"]
        },
        "receiverDeletedAt": {
            "type": ["integer", "null"]
        },
        "digest": {
            "type": "string"
        },
        "signature": {
            "type": ["string", "null"]
        },
        "signatureVersion": {
            "type": ["integer", "null"]
        },
        "clientReaction": to_nullable_object_schema(CLIENT_REACTION_INFO_SCHEMA),
        "reactions": to_nullable_object_schema(REACTION_TOTALS_INFO_SCHEMA),
    },
    "required": [
        "id",
        "bodySrcHash",
        "body",
        "heading",
        "createdAt",
        "digest",
    ],
    "additionalProperties": False
}

POSTING_REVISION_INFO_ARRAY_SCHEMA = array_schema(POSTING_REVISION_INFO_SCHEMA)

REACTION_CREATED_SCHEMA: Any = {
    "type": "object",
    "properties": {
        "reaction": to_nullable_object_schema(REACTION_INFO_SCHEMA),
        "totals": REACTION_TOTALS_INFO_SCHEMA,
    },
    "required": [
        "totals",
    ],
    "additionalProperties": False
}

SETTING_META_INFO_SCHEMA: Any = {
    "type": "object",
    "properties": {
        "name": {
            "type": "string"
        },
        "type": {
            "type": "string"
        },
        "defaultValue": {
            "type": ["string", "null"]
        },
        "privileged": {
            "type": ["boolean", "null"]
        },
        "title": {
            "type": "string"
        },
        "modifiers": to_nullable_object_schema(SETTING_TYPE_MODIFIERS_SCHEMA),
    },
    "required": [
        "name",
        "type",
        "title",
    ],
    "additionalProperties": False
}

SETTING_META_INFO_ARRAY_SCHEMA = array_schema(SETTING_META_INFO_SCHEMA)

STORY_SUMMARY_DATA_SCHEMA: Any = {
    "type": "object",
    "properties": {
        "node": to_nullable_object_schema(STORY_SUMMARY_NODE_SCHEMA),
        "posting": to_nullable_object_schema(STORY_SUMMARY_ENTRY_SCHEMA),
        "comment": to_nullable_object_schema(STORY_SUMMARY_ENTRY_SCHEMA),
        "comments": {
            "type": ["array", "null"],
            "items": STORY_SUMMARY_ENTRY_SCHEMA
        },
        "totalComments": {
            "type": ["integer", "null"]
        },
        "repliedTo": to_nullable_object_schema(STORY_SUMMARY_ENTRY_SCHEMA),
        "parentPosting": to_nullable_object_schema(STORY_SUMMARY_ENTRY_SCHEMA),
        "reaction": to_nullable_object_schema(STORY_SUMMARY_REACTION_SCHEMA),
        "reactions": {
            "type": ["array", "null"],
            "items": STORY_SUMMARY_REACTION_SCHEMA
        },
        "totalReactions": {
            "type": ["integer", "null"]
        },
        "feedName": {
            "type": ["string", "null"]
        },
        "subscriptionReason": {
            "type": ["string", "null"]
        },
        "friendGroup": to_nullable_object_schema(STORY_SUMMARY_FRIEND_GROUP_SCHEMA),
        "blocked": to_nullable_object_schema(STORY_SUMMARY_BLOCKED_SCHEMA),
        "sheriff": to_nullable_object_schema(STORY_SUMMARY_SHERIFF_SCHEMA),
        "description": {
            "type": ["string", "null"]
        },
    },
    "additionalProperties": False
}

COMMENT_INFO_SCHEMA: Any = {
    "type": "object",
    "properties": {
        "id": {
            "type": "string"
        },
        "ownerName": {
            "type": "string"
        },
        "ownerFullName": {
            "type": ["string", "null"]
        },
        "ownerGender": {
            "type": ["string", "null"]
        },
        "ownerAvatar": to_nullable_object_schema(AVATAR_IMAGE_SCHEMA),
        "postingId": {
            "type": "string"
        },
        "postingRevisionId": {
            "type": "string"
        },
        "revisionId": {
            "type": "string"
        },
        "totalRevisions": {
            "type": "integer"
        },
        "bodyPreview": {
            "type": ["string", "null"]
        },
        "bodySrc": {
            "type": ["string", "null"]
        },
        "bodySrcHash": {
            "type": "string"
        },
        "bodySrcFormat": {
            "type": ["string", "null"]
        },
        "body": {
            "type": "string"
        },
        "bodyFormat": {
            "type": ["string", "null"]
        },
        "media": {
            "type": ["array", "null"],
            "items": MEDIA_ATTACHMENT_SCHEMA
        },
        "heading": {
            "type": "string"
        },
        "repliedTo": to_nullable_object_schema(REPLIED_TO_SCHEMA),
        "moment": {
            "type": "integer"
        },
        "createdAt": {
            "type": "integer"
        },
        "editedAt": {
            "type": ["integer", "null"]
        },
        "deletedAt": {
            "type": ["integer", "null"]
        },
        "revisionCreatedAt": {
            "type": "integer"
        },
        "deadline": {
            "type": ["integer", "null"]
        },
        "digest": {
            "type": "string"
        },
        "signature": {
            "type": ["string", "null"]
        },
        "signatureVersion": {
            "type": ["integer", "null"]
        },
        "operations": to_nullable_object_schema(COMMENT_OPERATIONS_SCHEMA),
        "reactionOperations": to_nullable_object_schema(REACTION_OPERATIONS_SCHEMA),
        "ownerOperations": to_nullable_object_schema(COMMENT_OPERATIONS_SCHEMA),
        "seniorOperations": to_nullable_object_schema(COMMENT_OPERATIONS_SCHEMA),
        "blockedOperations": {
            "type": ["array", "null"],
            "items": {
                "type": "string"
            }
        },
        "sheriffMarks": {
            "type": ["array", "null"],
            "items": SHERIFF_MARK_SCHEMA
        },
        "acceptedReactions": to_nullable_object_schema(ACCEPTED_REACTIONS_SCHEMA),
        "clientReaction": to_nullable_object_schema(CLIENT_REACTION_INFO_SCHEMA),
        "seniorReaction": to_nullable_object_schema(CLIENT_REACTION_INFO_SCHEMA),
        "reactions": to_nullable_object_schema(REACTION_TOTALS_INFO_SCHEMA),
    },
    "required": [
        "id",
        "ownerName",
        "postingId",
        "postingRevisionId",
        "revisionId",
        "totalRevisions",
        "bodySrcHash",
        "body",
        "heading",
        "moment",
        "createdAt",
        "revisionCreatedAt",
        "digest",
    ],
    "additionalProperties": False
}

COMMENTS_SLICE_INFO_SCHEMA: Any = {
    "type": "object",
    "properties": {
        "before": {
            "type": "integer"
        },
        "after": {
            "type": "integer"
        },
        "comments": {
            "type": "array",
            "items": COMMENT_INFO_SCHEMA
        },
        "total": {
            "type": "integer"
        },
        "totalInPast": {
            "type": "integer"
        },
        "totalInFuture": {
            "type": "integer"
        },
    },
    "required": [
        "before",
        "after",
        "comments",
        "total",
        "totalInPast",
        "totalInFuture",
    ],
    "additionalProperties": False
}

DRAFT_INFO_SCHEMA: Any = {
    "type": "object",
    "properties": {
        "id": {
            "type": "string"
        },
        "draftType": {
            "type": "string"
        },
        "receiverName": {
            "type": "string"
        },
        "receiverPostingId": {
            "type": ["string", "null"]
        },
        "receiverCommentId": {
            "type": ["string", "null"]
        },
        "repliedToId": {
            "type": ["string", "null"]
        },
        "createdAt": {
            "type": "integer"
        },
        "editedAt": {
            "type": ["integer", "null"]
        },
        "deadline": {
            "type": ["integer", "null"]
        },
        "ownerFullName": {
            "type": ["string", "null"]
        },
        "ownerAvatar": to_nullable_object_schema(AVATAR_IMAGE_SCHEMA),
        "acceptedReactions": to_nullable_object_schema(ACCEPTED_REACTIONS_SCHEMA),
        "bodySrc": {
            "type": ["string", "null"]
        },
        "bodySrcFormat": {
            "type": ["string", "null"]
        },
        "body": {
            "type": "string"
        },
        "bodyFormat": {
            "type": ["string", "null"]
        },
        "media": {
            "type": ["array", "null"],
            "items": MEDIA_ATTACHMENT_SCHEMA
        },
        "heading": {
            "type": "string"
        },
        "publishAt": {
            "type": ["integer", "null"]
        },
        "updateInfo": to_nullable_object_schema(UPDATE_INFO_SCHEMA),
        "operations": to_nullable_object_schema(POSTING_OPERATIONS_SCHEMA),
        "commentOperations": to_nullable_object_schema(COMMENT_OPERATIONS_SCHEMA),
    },
    "required": [
        "id",
        "draftType",
        "receiverName",
        "createdAt",
        "body",
        "heading",
    ],
    "additionalProperties": False
}

DRAFT_INFO_ARRAY_SCHEMA = array_schema(DRAFT_INFO_SCHEMA)

ENTRY_INFO_SCHEMA: Any = {
    "type": "object",
    "properties": {
        "posting": to_nullable_object_schema(POSTING_INFO_SCHEMA),
        "comment": to_nullable_object_schema(COMMENT_INFO_SCHEMA),
    },
    "additionalProperties": False
}

ENTRY_INFO_ARRAY_SCHEMA = array_schema(ENTRY_INFO_SCHEMA)

PLUGIN_INFO_SCHEMA: Any = {
    "type": "object",
    "properties": {
        "nodeId": {
            "type": "string"
        },
        "local": {
            "type": "boolean"
        },
        "name": {
            "type": "string"
        },
        "title": {
            "type": ["string", "null"]
        },
        "description": {
            "type": ["string", "null"]
        },
        "location": {
            "type": ["string", "null"]
        },
        "acceptedEvents": {
            "type": ["array", "null"],
            "items": {
                "type": "string"
            }
        },
        "settings": {
            "type": ["array", "null"],
            "items": SETTING_META_INFO_SCHEMA
        },
        "tokenId": {
            "type": ["string", "null"]
        },
    },
    "required": [
        "nodeId",
        "local",
        "name",
    ],
    "additionalProperties": False
}

PLUGIN_INFO_ARRAY_SCHEMA = array_schema(PLUGIN_INFO_SCHEMA)

STORY_INFO_SCHEMA: Any = {
    "type": "object",
    "properties": {
        "id": {
            "type": "string"
        },
        "feedName": {
            "type": "string"
        },
        "storyType": {
            "type": "string"
        },
        "createdAt": {
            "type": "integer"
        },
        "publishedAt": {
            "type": "integer"
        },
        "pinned": {
            "type": ["boolean", "null"]
        },
        "moment": {
            "type": "integer"
        },
        "viewed": {
            "type": ["boolean", "null"]
        },
        "read": {
            "type": ["boolean", "null"]
        },
        "satisfied": {
            "type": ["boolean", "null"]
        },
        "summaryNodeName": {
            "type": ["string", "null"]
        },
        "summaryFullName": {
            "type": ["string", "null"]
        },
        "summaryAvatar": to_nullable_object_schema(AVATAR_IMAGE_SCHEMA),
        "summary": {
            "type": ["string", "null"]
        },
        "summaryData": to_nullable_object_schema(STORY_SUMMARY_DATA_SCHEMA),
        "trackingId": {
            "type": ["string", "null"]
        },
        "posting": to_nullable_object_schema(POSTING_INFO_SCHEMA),
        "postingId": {
            "type": ["string", "null"]
        },
        "comment": to_nullable_object_schema(COMMENT_INFO_SCHEMA),
        "commentId": {
            "type": ["string", "null"]
        },
        "remoteNodeName": {
            "type": ["string", "null"]
        },
        "remoteFullName": {
            "type": ["string", "null"]
        },
        "remotePostingId": {
            "type": ["string", "null"]
        },
        "remoteCommentId": {
            "type": ["string", "null"]
        },
        "remoteMediaId": {
            "type": ["string", "null"]
        },
        "operations": to_nullable_object_schema(STORY_OPERATIONS_SCHEMA),
    },
    "required": [
        "id",
        "feedName",
        "storyType",
        "createdAt",
        "publishedAt",
        "moment",
    ],
    "additionalProperties": False
}

COMMENT_CREATED_SCHEMA: Any = {
    "type": "object",
    "properties": {
        "comment": COMMENT_INFO_SCHEMA,
        "total": {
            "type": "integer"
        },
    },
    "required": [
        "comment",
        "total",
    ],
    "additionalProperties": False
}

FEED_SLICE_INFO_SCHEMA: Any = {
    "type": "object",
    "properties": {
        "before": {
            "type": "integer"
        },
        "after": {
            "type": "integer"
        },
        "stories": {
            "type": "array",
            "items": STORY_INFO_SCHEMA
        },
        "totalInPast": {
            "type": "integer"
        },
        "totalInFuture": {
            "type": "integer"
        },
    },
    "required": [
        "before",
        "after",
        "stories",
        "totalInPast",
        "totalInFuture",
    ],
    "additionalProperties": False
}

PUSH_CONTENT_SCHEMA: Any = {
    "type": "object",
    "properties": {
        "type": {
            "type": "string"
        },
        "id": {
            "type": ["string", "null"]
        },
        "story": to_nullable_object_schema(STORY_INFO_SCHEMA),
        "feedStatus": to_nullable_object_schema(FEED_WITH_STATUS_SCHEMA),
    },
    "required": [
        "type",
    ],
    "additionalProperties": False
}

PUSH_CONTENT_ARRAY_SCHEMA = array_schema(PUSH_CONTENT_SCHEMA)
