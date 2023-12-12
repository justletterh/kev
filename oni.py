import subprocess as subp
from onami.features.baseclass import Feature
from onami.cog import OPTIONAL_FEATURES, STANDARD_FEATURES
import re


class Onih(*OPTIONAL_FEATURES, *STANDARD_FEATURES):
    @Feature.Command(parent="oni", name="dm", aliases=["pm"])
    async def oni_dm(self, ctx, user, *, msg=None):
        if msg == None:
            await ctx.send("Please specify a message to dm to user.")
            return
        reg = re.compile("^<@!?([0-9]+)>$")
        h = reg.match(user)
        if h != None:
            user = await self.bot.fetch_user(h.group(1))
            await user.send(msg)
            await ctx.send("Done! :white_check_mark:")
        else:
            await ctx.send("Please mention a user before the message.")
            return

    @Feature.Command(
        parent="oni",
        name="multidm",
        aliases=["multi_dm", "multi-dm", "multi_pm", "multi-pm", "multipm"],
    )
    async def oni_multidm(self, ctx, user, x, *, msg=None):
        try:
            x = int(x)
        except ValueError:
            await ctx.send("The number of messages to send should be a whole number.")
            return
        if msg == None:
            await ctx.send("Please specify a message to dm to user.")
            return
        reg = re.compile("^<@!?([0-9]+)>$")
        h = reg.match(user)
        if h != None:
            user = await self.bot.fetch_user(h.group(1))
            if x > 5:
                await ctx.send("Sending...")
            for _ in range(x):
                await user.send(msg)
            await ctx.send("Done! :white_check_mark:")
        else:
            await ctx.send("Please mention a user before the message.")
            return

    @Feature.Command(
        parent="oni",
        name="pyfile",
        aliases=["pythonfile", "py-file", "python-file", "pyf", "pythonf"],
    )
    async def oni_pyfile(self, ctx, file):
        proc = subp.Popen(
            f"python3 {file}", shell=True, stdout=subp.PIPE, stderr=subp.PIPE
        )
        stdout, stderr = proc.communicate()
        stdout = stdout.decode("utf-8")
        stderr = stderr.decode("utf-8")
        if stderr != "":
            await ctx.send(f"Something went wrong :sad: :\n```\n{stderr}\n```")
        elif stdout != "":
            await ctx.send(f"```\n{stdout}\n```")
        else:
            await ctx.send("Done! :white_check_mark:")

    @Feature.Command(
        parent="oni",
        name="js",
        aliases=["nodejs", "node-js", "node", "javascript", "nodejavascript"],
    )
    async def oni_js(self, ctx, *, args=None):
        if args == None:
            await ctx.send("Please input some NodeJS code")
            return
        text = args
        if text.lower().startswith("```js"):
            text = text[6 : len(text)]
        elif text.startswith("```"):
            text = text[4 : len(text)]
        if text.endswith("```"):
            text = text[0 : len(text) - 4]
        text = text.replace('"', '\\"')
        proc = subp.Popen(
            f'nodejs -e "{text}"', shell=True, stdout=subp.PIPE, stderr=subp.PIPE
        )
        stdout, stderr = proc.communicate()
        stdout = stdout.decode("utf-8")
        stderr = stderr.decode("utf-8")
        if stdout.endswith("\n"):
            stdout = stdout[0 : len(stdout) - 1]
        if stderr != "":
            await ctx.send(f"Something went wrong :sad: :\n```\n{stderr}\n```")
        elif stdout != "":
            await ctx.send(f"```\n{stdout}\n```")
        else:
            await ctx.send("Done! :white_check_mark:")

    @Feature.Command(
        parent="oni",
        name="jsfile",
        aliases=[
            "js-file",
            "nodefile",
            "node-file",
            "nodejsfile",
            "nodejs-file",
            "javascriptfile",
            "javascript-file",
            "nodejavascriptfile",
            "nodejavascript-file",
            "jsf",
            "nodef",
            "nodejsf",
            "javascriptf",
            "nodejavascriptf",
        ],
    )
    async def oni_jsfile(self, ctx, file):
        proc = subp.Popen(
            f"nodejs {file}", shell=True, stdout=subp.PIPE, stderr=subp.PIPE
        )
        stdout, stderr = proc.communicate()
        stdout = stdout.decode("utf-8")
        stderr = stderr.decode("utf-8")
        if stderr != "":
            await ctx.send(f"Something went wrong :sad: :\n```\n{stderr}\n```")
        elif stdout != "":
            await ctx.send(f"```\n{stdout}\n```")
        else:
            await ctx.send("Done! :white_check_mark:")

    @Feature.Command(parent="oni", name="rb", aliases=["ruby"])
    async def oni_rb(self, ctx, *, args=None):
        if args == None:
            await ctx.send("Please input some Ruby code")
            return
        text = args
        if text.lower().startswith("```rb"):
            text = text[6 : len(text)]
        elif text.startswith("```"):
            text = text[4 : len(text)]
        if text.endswith("```"):
            text = text[0 : len(text) - 4]
        text = text.replace('"', '\\"')
        proc = subp.Popen(
            f'ruby -e "{text}"', shell=True, stdout=subp.PIPE, stderr=subp.PIPE
        )
        stdout, stderr = proc.communicate()
        stdout = stdout.decode("utf-8")
        stderr = stderr.decode("utf-8")
        if stdout.endswith("\n"):
            stdout = stdout[0 : len(stdout) - 1]
        if stderr != "":
            await ctx.send(f"Something went wrong :sad: :\n```\n{stderr}\n```")
        elif stdout != "":
            await ctx.send(f"```\n{stdout}\n```")
        else:
            await ctx.send("Done! :white_check_mark:")

    @Feature.Command(
        parent="oni",
        name="rbfile",
        aliases=["rubyfile", "rb-file", "ruby-file", "rubyf", "rbf"],
    )
    async def oni_rbfile(self, ctx, file):
        proc = subp.Popen(
            f"ruby {file}", shell=True, stdout=subp.PIPE, stderr=subp.PIPE
        )
        stdout, stderr = proc.communicate()
        stdout = stdout.decode("utf-8")
        stderr = stderr.decode("utf-8")
        if stderr != "":
            await ctx.send(f"Something went wrong :sad: :\n```\n{stderr}\n```")
        elif stdout != "":
            await ctx.send(f"```\n{stdout}\n```")
        else:
            await ctx.send("Done! :white_check_mark:")

    @Feature.Command(parent="oni", name="lua")
    async def oni_lua(self, ctx, *, args=None):
        if args == None:
            await ctx.send("Please input some Lua code")
            return
        text = args
        if text.lower().startswith("```lua"):
            text = text[7 : len(text)]
        elif text.startswith("```"):
            text = text[4 : len(text)]
        if text.endswith("```"):
            text = text[0 : len(text) - 4]
        text = text.replace('"', '\\"')
        proc = subp.Popen(
            f'lua -e "{text}"', shell=True, stdout=subp.PIPE, stderr=subp.PIPE
        )
        stdout, stderr = proc.communicate()
        stdout = stdout.decode("utf-8")
        stderr = stderr.decode("utf-8")
        if stdout.endswith("\n"):
            stdout = stdout[0 : len(stdout) - 1]
        if stderr != "":
            await ctx.send(f"Something went wrong :sad: :\n```\n{stderr}\n```")
        elif stdout != "":
            await ctx.send(f"```\n{stdout}\n```")
        else:
            await ctx.send("Done! :white_check_mark:")

    @Feature.Command(parent="oni", name="luafile", aliases=["lua-file", "luaf"])
    async def oni_luafile(self, ctx, file):
        proc = subp.Popen(f"lua {file}", shell=True, stdout=subp.PIPE, stderr=subp.PIPE)
        stdout, stderr = proc.communicate()
        stdout = stdout.decode("utf-8")
        stderr = stderr.decode("utf-8")
        if stderr != "":
            await ctx.send(f"Something went wrong :sad: :\n```\n{stderr}\n```")
        elif stdout != "":
            await ctx.send(f"```\n{stdout}\n```")
        else:
            await ctx.send("Done! :white_check_mark:")

    @Feature.Command(parent="oni", name="php")
    async def oni_php(self, ctx, *, args=None):
        if args == None:
            await ctx.send("Please input some PHP-CLI code")
            return
        text = args
        if text.lower().startswith("```php"):
            text = text[7 : len(text)]
        elif text.startswith("```"):
            text = text[4 : len(text)]
        if text.endswith("```"):
            text = text[0 : len(text) - 4]
        if text.lower().startswith("<?php"):
            text = text[6 : len(text)]
        text = text.replace('"', '\\"')
        proc = subp.Popen(
            f'php -r "{text}"', shell=True, stdout=subp.PIPE, stderr=subp.PIPE
        )
        stdout, stderr = proc.communicate()
        stdout = stdout.decode("utf-8")
        stderr = stderr.decode("utf-8")
        if stdout.endswith("\n"):
            stdout = stdout[0 : len(stdout) - 1]
        if stderr != "":
            await ctx.send(f"Something went wrong :sad: :\n```\n{stderr}\n```")
        elif stdout != "":
            await ctx.send(f"```\n{stdout}\n```")
        else:
            await ctx.send("Done! :white_check_mark:")

    @Feature.Command(parent="oni", name="phpfile", aliases=["php-file", "phpf"])
    async def oni_phpfile(self, ctx, file):
        proc = subp.Popen(
            f"php -f {file}", shell=True, stdout=subp.PIPE, stderr=subp.PIPE
        )
        stdout, stderr = proc.communicate()
        stdout = stdout.decode("utf-8")
        stderr = stderr.decode("utf-8")
        if stderr != "":
            await ctx.send(f"Something went wrong :sad: :\n```\n{stderr}\n```")
        elif stdout != "":
            await ctx.send(f"```\n{stdout}\n```")
        else:
            await ctx.send("Done! :white_check_mark:")

    @Feature.Command(parent="oni", name="pl", aliases=["perl"])
    async def oni_pl(self, ctx, *, args=None):
        if args == None:
            await ctx.send("Please input some Perl code")
            return
        text = args
        if text.lower().startswith("```pl"):
            text = text[6 : len(text)]
        elif text.startswith("```"):
            text = text[4 : len(text)]
        if text.endswith("```"):
            text = text[0 : len(text) - 4]
        text = text.replace('"', '\\"')
        proc = subp.Popen(
            f'perl -e "{text}"', shell=True, stdout=subp.PIPE, stderr=subp.PIPE
        )
        stdout, stderr = proc.communicate()
        stdout = stdout.decode("utf-8")
        stderr = stderr.decode("utf-8")
        if stdout.endswith("\n"):
            stdout = stdout[0 : len(stdout) - 1]
        if stderr != "":
            await ctx.send(f"Something went wrong :sad: :\n```\n{stderr}\n```")
        elif stdout != "":
            await ctx.send(f"```\n{stdout}\n```")
        else:
            await ctx.send("Done! :white_check_mark:")

    @Feature.Command(
        parent="oni",
        name="plfile",
        aliases=["perlfile", "pl-file", "perl-file", "perlf", "plf"],
    )
    async def oni_plfile(self, ctx, file):
        proc = subp.Popen(
            f"perl {file}", shell=True, stdout=subp.PIPE, stderr=subp.PIPE
        )
        stdout, stderr = proc.communicate()
        stdout = stdout.decode("utf-8")
        stderr = stderr.decode("utf-8")
        if stderr != "":
            await ctx.send(f"Something went wrong :sad: :\n```\n{stderr}\n```")
        elif stdout != "":
            await ctx.send(f"```\n{stdout}\n```")
        else:
            await ctx.send("Done! :white_check_mark:")

    @Feature.Command(parent="oni", name="clj", aliases=["clojure"])
    async def oni_clj(self, ctx, *, args=None):
        if args == None:
            await ctx.send("Please input some Clojure code")
            return
        text = args
        if text.lower().startswith("```clj"):
            text = text[7 : len(text)]
        elif text.startswith("```"):
            text = text[4 : len(text)]
        if text.endswith("```"):
            text = text[0 : len(text) - 4]
        text = text.replace('"', '\\"')
        proc = subp.Popen(
            f'clojure -e "{text}"', shell=True, stdout=subp.PIPE, stderr=subp.PIPE
        )
        stdout, stderr = proc.communicate()
        stdout = stdout.decode("utf-8")
        stderr = stderr.decode("utf-8")
        if stdout.endswith("\n"):
            stdout = stdout[0 : len(stdout) - 1]
        if stderr != "":
            await ctx.send(f"Something went wrong :sad: :\n```\n{stderr}\n```")
        elif stdout != "":
            await ctx.send(f"```\n{stdout}\n```")
        else:
            await ctx.send("Done! :white_check_mark:")

    @Feature.Command(
        parent="oni",
        name="cljfile",
        aliases=["clojurefile", "clj-file", "clojure-file", "clojuref", "cljf"],
    )
    async def oni_cljfile(self, ctx, file):
        proc = subp.Popen(
            f"clojure {file}", shell=True, stdout=subp.PIPE, stderr=subp.PIPE
        )
        stdout, stderr = proc.communicate()
        stdout = stdout.decode("utf-8")
        stderr = stderr.decode("utf-8")
        if stderr != "":
            await ctx.send(f"Something went wrong :sad: :\n```\n{stderr}\n```")
        elif stdout != "":
            await ctx.send(f"```\n{stdout}\n```")
        else:
            await ctx.send("Done! :white_check_mark:")

#    @Feature.Command(parent="oni", name="bf", aliases=["brainfuck"])
#    async def oni_clj(self, ctx, *, args=None):
#        if args == None:
#            await ctx.send("Please input some Brain||Fuck|| code")
#            return
#        text = args
#        if text.lower().startswith("```bf"):
#            text = text[6 : len(text)]
#        elif text.startswith("```"):
#            text = text[4 : len(text)]
#        if text.endswith("```"):
#            text = text[0 : len(text) - 4]
#        text = text.replace('"', '\\"')
#        proc = subp.Popen(
#            f'clojure -e "{text}"', shell=True, stdout=subp.PIPE, stderr=subp.PIPE
#        )
#        stdout, stderr = proc.communicate()
#        stdout = stdout.decode("utf-8")
#        stderr = stderr.decode("utf-8")
#        if stdout.endswith("\n"):
#            stdout = stdout[0 : len(stdout) - 1]
#        if stderr != "":
#            await ctx.send(f"Something went wrong :sad: :\n```\n{stderr}\n```")
#        elif stdout != "":
#            await ctx.send(f"```\n{stdout}\n```")
#        else:
#            await ctx.send("Done! :white_check_mark:")

    @Feature.Command(
        parent="oni",
        name="bffile",
        aliases=["brainfuckfile", "bf-file", "brianfuck-file", "brainfuckf", "bff"],
    )
    async def oni_cljfile(self, ctx, file):
        proc = subp.Popen(
            f"beef {file}", shell=True, stdout=subp.PIPE, stderr=subp.PIPE
        )
        stdout, stderr = proc.communicate()
        stdout = stdout.decode("utf-8")
        stderr = stderr.decode("utf-8")
        if stderr != "":
            await ctx.send(f"Something went wrong :sad: :\n```\n{stderr}\n```")
        elif stdout != "":
            await ctx.send(f"```\n{stdout}\n```")
        else:
            await ctx.send("Done! :white_check_mark:")