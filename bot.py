import discord
from discord.ext import commands
import asyncio
import random
import time


# =========================
# 🔑 CONFIG
# =========================


TOKEN = "MTQ5NTc4NTgwNDc4MDQwODk3Mg.G_EFdT.BW_nefWIK3mRFL4U1fVr9n37tKJqTZlfNMVkCA"

intents = discord.Intents.default()

intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)




# =========================
# 🔄 READY + GLOBAL SYNC
# =========================


@bot.event
async def on_ready():
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} slash commands globally")
    except Exception as e:
        print("Sync error:", e)

    print(f"Bot online as {bot.user}")




# =========================
# 🤝 TEAM JOIN
# =========================


@bot.tree.command(name="teamjoin", description="Add user to team")
async def teamjoin(interaction: discord.Interaction, wer: discord.Member, rang: str, grund: str, mfg: str):

    role = discord.utils.get(interaction.guild.roles, name=rang)
    if role:
        await wer.add_roles(role)

    embed = discord.Embed(title="🤝 TEAM JOIN", color=discord.Color.green())
    embed.add_field(name="Wer", value=wer.mention, inline=True)
    embed.add_field(name="Rang", value=rang, inline=True)
    embed.add_field(name="Grund", value=grund, inline=False)
    embed.add_field(name="MFG", value=mfg, inline=False)

    await interaction.response.send_message(embed=embed)






# =========================
# ⚠️ TEAM WARN
# =========================


@bot.tree.command(name="teamwarn", description="Warn user")
async def teamwarn(interaction: discord.Interaction, wer: discord.Member, wie_viele: int, grund: str, mfg: str):

    embed = discord.Embed(title="⚠️ TEAM WARN", color=discord.Color.orange())
    embed.add_field(name="Wer", value=wer.mention)
    embed.add_field(name="Anzahl", value=str(wie_viele))
    embed.add_field(name="Grund", value=grund)
    embed.add_field(name="MFG", value=mfg)

    await interaction.response.send_message(embed=embed)






# =========================
# 🚪 TEAM LEAVE
# =========================


@bot.tree.command(name="teamleave", description="Remove user from team")
async def teamleave(interaction: discord.Interaction, wer: discord.Member, rang: str, grund: str, mfg: str):

    role = discord.utils.get(interaction.guild.roles, name=rang)
    if role:
        await wer.remove_roles(role)

    embed = discord.Embed(title="🚪 TEAM LEAVE", color=discord.Color.blue())
    embed.add_field(name="Wer", value=wer.mention)
    embed.add_field(name="Rang", value=rang)
    embed.add_field(name="Grund", value=grund)
    embed.add_field(name="MFG", value=mfg)

    await interaction.response.send_message(embed=embed)






# =========================
# ❌ TEAM KICK
# =========================


@bot.tree.command(name="teamkick", description="Kick user")
async def teamkick(interaction: discord.Interaction, wer: discord.Member, grund: str, mfg: str):

    await wer.kick(reason=grund)

    embed = discord.Embed(title="❌ TEAM KICK", color=discord.Color.red())
    embed.add_field(name="Wer", value=wer.mention)
    embed.add_field(name="Grund", value=grund)
    embed.add_field(name="MFG", value=mfg)

    await interaction.response.send_message(embed=embed)






# =========================
# ⬆️ UPRANK
# =========================


@bot.tree.command(name="uprank", description="Promote user")
async def uprank(interaction: discord.Interaction, wer: discord.Member, rang: str, grund: str, mfg: str):

    role = discord.utils.get(interaction.guild.roles, name=rang)
    if role:
        await wer.add_roles(role)

    embed = discord.Embed(title="⬆️ UPRANK", color=discord.Color.green())
    embed.add_field(name="Wer", value=wer.mention)
    embed.add_field(name="Rang", value=rang)
    embed.add_field(name="Grund", value=grund)
    embed.add_field(name="MFG", value=mfg)

    await interaction.response.send_message(embed=embed)






# =========================
# ⬇️ DOWNRANK
# =========================


@bot.tree.command(name="downrank", description="Demote user")
async def downrank(interaction: discord.Interaction, wer: discord.Member, rang: str, grund: str, mfg: str):

    role = discord.utils.get(interaction.guild.roles, name=rang)
    if role:
        await wer.remove_roles(role)

    embed = discord.Embed(title="⬇️ DOWNRANK", color=discord.Color.red())
    embed.add_field(name="Wer", value=wer.mention)
    embed.add_field(name="Rang", value=rang)
    embed.add_field(name="Grund", value=grund)
    embed.add_field(name="MFG", value=mfg)

    await interaction.response.send_message(embed=embed)





# =========================
# 🚀 START BOT
# =========================

bot.run("MTQ5NTc4NTgwNDc4MDQwODk3Mg.G_EFdT.BW_nefWIK3mRFL4U1fVr9n37tKJqTZlfNMVkCA")  