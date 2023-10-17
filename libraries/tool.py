import time


def hash(qq: int):
    days = int(time.strftime("%d", time.localtime(time.time()))) + 31 * int(
        time.strftime("%m", time.localtime(time.time()))) + 77
    return (days * qq) >> 8


def hash_shift_date(qq: int, shift: int):
    timestamp = time.time() + shift * 86400
    month = int(time.strftime("%m", time.localtime(timestamp)))
    date = int(time.strftime("%d", time.localtime(timestamp)))
    days = date + 31 * month + 77
    return (days * qq) >> 8, month, date


def render_forward_msg(msg_list: list, uid: int=10001, name: str='maimaiDX'):
    forward_msg = []
    for msg in msg_list:
        forward_msg.append({
            "type": "node",
            "data": {
                "name": str(name),
                "uin": str(uid),
                "content": msg
            }
        })
    return forward_msg
