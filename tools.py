import ast, re, json, webcolors
from scipy.spatial import KDTree


def evaluate_expr(expr):
    if isinstance(expr, ast.Expression):
        return evaluate_expr(expr.body)
    elif isinstance(expr, ast.Num):
        return expr.n
    elif isinstance(expr, ast.BinOp):
        op = expr.op
        left = evaluate_expr(expr.left)
        right = evaluate_expr(expr.right)
        if isinstance(op, ast.Add):
            return left + right
        elif isinstance(op, ast.Mult):
            return left * right
        elif isinstance(op, ast.Div):
            return left / right
    raise ValueError(f"Can't evaluate {expr}")


meth = lambda s: evaluate_expr(ast.parse(s, mode="eval").body)


class Bot:
    def __init__(
        self,
        token,
        name,
        status,
        guilds,
        anon_channel,
        anon_log,
        anon_log_channel,
        owners,
        pfx="$",
        color=0xFF0000,
    ):
        self.token = token
        self.pfx = pfx
        self.name = name
        self.color = color
        self.status = status
        self.guilds = guilds
        self.anon_channel = anon_channel
        self.anon_log = anon_log
        self.anon_log_channel = anon_log_channel
        self.owners = owners


class Status:
    def __init__(self, text, value="online"):
        self.text = text
        value = re.sub("[^a-z]+", "", value.lower())
        if value == "away":
            self.value = "idle"
        elif value not in ["online", "offline", "dnd", "idle"]:
            self.value = "online"
        else:
            self.value = value


def get_settings(fn):
    f = open(fn, "r")
    d = f.read()
    f.close()
    d = json.loads(d)
    d["color"] = int("0x" + d["color"], 16)
    b = Bot(
        token=d["token"],
        name=d["name"],
        status=Status(value=d["status"], text=d["status_text"]),
        color=d["color"],
        guilds=d["guilds"],
        anon_channel=d["confession_channel"],
        anon_log=d["log_confession"],
        anon_log_channel=d["confession_log_channel"],
        owners=d["owner_ids"],
        pfx=d["prefix"],
    )
    return b


def hex2rgb(hex):
    hex = re.sub("#", "", hex)
    r = int(hex[0:2], 16)
    g = int(hex[2:4], 16)
    b = int(hex[4:6], 16)
    return (r, g, b)

hex2word = lambda x: webcolors.hex_to_name(x)