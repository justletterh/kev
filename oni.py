import subprocess as subp
from onami.features.baseclass import Feature
from onami.cog import OPTIONAL_FEATURES, STANDARD_FEATURES

class Onih(*OPTIONAL_FEATURES, *STANDARD_FEATURES):
    @Feature.Command(parent="oni", name="pyfile")
    async def oni_pyfile(self, ctx, file):
        proc=subp.Popen(f"python3 {file}", shell=True, stdout=subp.PIPE, stderr=subp.PIPE)
        stdout, stderr=proc.communicate()
        stdout=stdout.decode("utf-8")
        stderr=stderr.decode("utf-8")
        if stderr!="":
            await ctx.send(f"Something went wrong :sad: :\n```\n{stderr}\n```")
        elif stdout!="":
            await ctx.send(f"```\n{stdout}\n```")
        else:
            await ctx.send("Done!!!")
    @Feature.Command(parent="oni", name="js")
    async def oni_js(self, ctx, *, args=None):
        if args==None:
            await ctx.send("Please input some NodeJS code")
            return
        text=args
        if text.lower().startswith("```js"):
            text=text[6:len(text)]
        elif text.startswith("```"):
            text=text[4:len(text)]
        if text.endswith("```"):
            text=text[0:len(text)-4]
        text=text.replace('"','\\"')
        proc=subp.Popen(f'nodejs -e "{text}"', shell=True, stdout=subp.PIPE, stderr=subp.PIPE)
        stdout, stderr=proc.communicate()
        stdout=stdout.decode("utf-8")
        stderr=stderr.decode("utf-8")
        if stdout.endswith("\n"):
            stdout=stdout[0:len(stdout)-1]
        if stderr!="":
            await ctx.send(f"Something went wrong :sad: :\n```\n{stderr}\n```")
        elif stdout!="":
            await ctx.send(f"```\n{stdout}\n```")
        else:
            await ctx.send("Done!!!")
    @Feature.Command(parent="oni", name="jsfile")
    async def oni_jsfile(self, ctx, file):
        proc=subp.Popen(f"nodejs {file}", shell=True, stdout=subp.PIPE, stderr=subp.PIPE)
        stdout, stderr=proc.communicate()
        stdout=stdout.decode("utf-8")
        stderr=stderr.decode("utf-8")
        if stderr!="":
            await ctx.send(f"Something went wrong :sad: :\n```\n{stderr}\n```")
        elif stdout!="":
            await ctx.send(f"```\n{stdout}\n```")
        else:
            await ctx.send("Done!!!")
    @Feature.Command(parent="oni", name="rb")
    async def oni_rb(self, ctx, *, args=None):
        if args==None:
            await ctx.send("Please input some Ruby code")
            return
        text=args
        if text.lower().startswith("```rb"):
            text=text[6:len(text)]
        elif text.startswith("```"):
            text=text[4:len(text)]
        if text.endswith("```"):
            text=text[0:len(text)-4]
        text=text.replace('"','\\"')
        proc=subp.Popen(f'ruby -e "{text}"', shell=True, stdout=subp.PIPE, stderr=subp.PIPE)
        stdout, stderr=proc.communicate()
        stdout=stdout.decode("utf-8")
        stderr=stderr.decode("utf-8")
        if stdout.endswith("\n"):
            stdout=stdout[0:len(stdout)-1]
        if stderr!="":
            await ctx.send(f"Something went wrong :sad: :\n```\n{stderr}\n```")
        elif stdout!="":
            await ctx.send(f"```\n{stdout}\n```")
        else:
            await ctx.send("Done!!!")
    @Feature.Command(parent="oni", name="rbfile")
    async def oni_rbfile(self, ctx, file):
        proc=subp.Popen(f"ruby {file}", shell=True, stdout=subp.PIPE, stderr=subp.PIPE)
        stdout, stderr=proc.communicate()
        stdout=stdout.decode("utf-8")
        stderr=stderr.decode("utf-8")
        if stderr!="":
            await ctx.send(f"Something went wrong :sad: :\n```\n{stderr}\n```")
        elif stdout!="":
            await ctx.send(f"```\n{stdout}\n```")
        else:
            await ctx.send("Done!!!")
    @Feature.Command(parent="oni", name="lua")
    async def oni_lua(self, ctx, *, args=None):
        if args==None:
            await ctx.send("Please input some Lua code")
            return
        text=args
        if text.lower().startswith("```lua"):
            text=text[7:len(text)]
        elif text.startswith("```"):
            text=text[4:len(text)]
        if text.endswith("```"):
            text=text[0:len(text)-4]
        text=text.replace('"','\\"')
        proc=subp.Popen(f'lua -e "{text}"', shell=True, stdout=subp.PIPE, stderr=subp.PIPE)
        stdout, stderr=proc.communicate()
        stdout=stdout.decode("utf-8")
        stderr=stderr.decode("utf-8")
        if stdout.endswith("\n"):
            stdout=stdout[0:len(stdout)-1]
        if stderr!="":
            await ctx.send(f"Something went wrong :sad: :\n```\n{stderr}\n```")
        elif stdout!="":
            await ctx.send(f"```\n{stdout}\n```")
        else:
            await ctx.send("Done!!!")
    @Feature.Command(parent="oni", name="luafile")
    async def oni_luafile(self, ctx, file):
        proc=subp.Popen(f"lua {file}", shell=True, stdout=subp.PIPE, stderr=subp.PIPE)
        stdout, stderr=proc.communicate()
        stdout=stdout.decode("utf-8")
        stderr=stderr.decode("utf-8")
        if stderr!="":
            await ctx.send(f"Something went wrong :sad: :\n```\n{stderr}\n```")
        elif stdout!="":
            await ctx.send(f"```\n{stdout}\n```")
        else:
            await ctx.send("Done!!!")
    @Feature.Command(parent="oni", name="php")
    async def oni_php(self, ctx, *, args=None):
        if args==None:
            await ctx.send("Please input some PHP-CLI code")
            return
        text=args
        if text.lower().startswith("```php"):
            text=text[7:len(text)]
        elif text.startswith("```"):
            text=text[4:len(text)]
        if text.endswith("```"):
            text=text[0:len(text)-4]
        if text.lower().startswith("<?php"):
            text=text[6:len(text)]
        text=text.replace('"','\\"')
        proc=subp.Popen(f'php -r "{text}"', shell=True, stdout=subp.PIPE, stderr=subp.PIPE)
        stdout, stderr=proc.communicate()
        stdout=stdout.decode("utf-8")
        stderr=stderr.decode("utf-8")
        if stdout.endswith("\n"):
            stdout=stdout[0:len(stdout)-1]
        if stderr!="":
            await ctx.send(f"Something went wrong :sad: :\n```\n{stderr}\n```")
        elif stdout!="":
            await ctx.send(f"```\n{stdout}\n```")
        else:
            await ctx.send("Done!!!")
    @Feature.Command(parent="oni", name="phpfile")
    async def oni_phpfile(self, ctx, file):
        proc=subp.Popen(f"php -f {file}", shell=True, stdout=subp.PIPE, stderr=subp.PIPE)
        stdout, stderr=proc.communicate()
        stdout=stdout.decode("utf-8")
        stderr=stderr.decode("utf-8")
        if stderr!="":
            await ctx.send(f"Something went wrong :sad: :\n```\n{stderr}\n```")
        elif stdout!="":
            await ctx.send(f"```\n{stdout}\n```")
        else:
            await ctx.send("Done!!!")