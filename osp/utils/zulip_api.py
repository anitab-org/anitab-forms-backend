from zulip import Client

# By default the API key file you download is named as 'download' by Zulip. You can place
# this file one directory previous to the cuurent directory your file is in
client = Client(config_file="download")


def get_zulip_user(zulip_id: int) -> dict:
    """Takes the target's user ID as an argument and returns a dictionary containing
    basic data on the Zulip user associated with that id

    Example usage:

            >>> get_zulip_user(5)
            {"avatar_url": "...","bot_type": null,... "profile_data":...}
    """

    result = client.get_user_by_id(zulip_id)
    print(result)
    return result["user"]


def get_total_messages_count(zulip_id: int) -> int:
    """Takes the target's user id: int as arguement and returns the total number of messages: int sent by the
    user associated with that id if total messages is less than 5000
      it returns 5000: int if the actual total numbers of messages is greater than 5000

      Example usage:

            >>> get_total_messages(5)
            10
    """

    request = {
        "anchor": "newest",
        "num_before": 5000,
        "num_after": 0,
        "narrow": [{"operator": "sender", "operand": f"user{zulip_id}@zulipchat.com"}],
    }
    result = client.get_messages(request)
    result = len(result["messages"])
    return result


def get_newest_message(zulip_id: int) -> dict:
    """Takes the target's user ID: int as an arguement and returns a dictionary containing requested information
    about the most recent message sent by user associated with the given user id

    Example usage:

            >>> get_newest_message(5)
            {"avatar_url": ...,"bot_type": null, ..., "profile_data":...}
    """

    request = {
        "anchor": "newest",
        "num_before": 1,
        "num_after": 0,
        "narrow": [{"operator": "sender", "operand": f"user{zulip_id}@zulipchat.com"}],
    }
    result = client.get_messages(request)
    result = result["messages"]
    return result


def get_stream_messages(stream: str, zulip_id: int) -> int:
    """It takes stream name: string and target id: int as arguements
    and returns the total number of messages sent on the given stream: int, by user associated with given user id

    Example usage:

            >>> get_stream_messages(announce,5)
            10
    """

    request = {
        "anchor": "newest",
        "num_before": 1,
        "num_after": 0,
        "narrow": [
            {"operator": "sender", "operand": f"user{zulip_id}@zulipchat.com"},
            {"operator": "stream", "operand": f"{stream}"},
        ],
    }
    result = client.get_messages(request)
    result = len(result["messages"])
    return result
