import random
from pyrogram import Client
from QuotesBot.heart import brainy_quotes, main
from QuotesBot.qod import quote_of_the_day
from QuotesBot.random_quotes import random_quote
from QuotesBot.bot_users import check_for_user


# Inline System
@Client.on_inline_query()
async def answer(_, query):
    if query.query == "":
        await query.answer(
            results=[main],
            switch_pm_text="Learn How to use me",
            switch_pm_parameter="start"
        )
    elif query.query in ["#q", "#qod"]:
        results = await quote_of_the_day()
        await query.answer(
            results,
            switch_pm_text="Learn How to use me",
            switch_pm_parameter="start"
        )
    elif query.query in ["#r", "#random"]:
        result = await random_quote()
        await query.answer(
            [result],
            switch_pm_text="Learn How to use me",
            switch_pm_parameter="start"
        )
    elif query.query.endswith("#1"):
        the_query = query.query.rsplit(' ', 1)[0]
        results = await brainy_quotes(the_query)
        result = random.choice(results)
        await query.answer(
            [result],
            switch_pm_text="Learn How to use me",
            switch_pm_parameter="start"
        )
    else:
        results = await brainy_quotes(query.query)
        await query.answer(
            results,
            switch_pm_text="Learn How to use me",
            switch_pm_parameter="start"
        )
    await check_for_user(query.from_user.id)
