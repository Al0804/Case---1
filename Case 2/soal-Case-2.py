comments = [
    {
        "commentId": 1,
        "commentContent": "Hai",
        "replies": [
            {
                "commentId": 11,
                "commentContent": "Hai juga",
                "replies": [
                    {"commentId": 111, "commentContent": "Haai juga hai jugaa"},
                    {"commentId": 112, "commentContent": "Haai juga hai jugaa"},
                ],
            },
            {
                "commentId": 12,
                "commentContent": "Hai juga",
                "replies": [
                    {"commentId": 121, "commentContent": "Haai juga hai jugaa"}
                ],
            },
        ],
    },
    {"commentId": 2, "commentContent": "Halooo"},
]

def count_comments(comments):
    count = 0
    for comment in comments:
        count += 1
        if "replies" in comment:
            count += count_comments(comment["replies"])
    return count


total_comments = count_comments(comments)
print("Total komentar", total_comments)
