from aiogram.types import BotCommand


async def set_commands_menu(bot):
    """
        Set up the main menu commands for the bot.
        Args:
            bot (telegram.Bot): The Telegram bot instance.
        Returns:
            None
        """
    main_menu_commands = [
        BotCommand(command='/start',
                   description='Запустить бота'),
        BotCommand(command='/stop',
                   description='Остановить бота'),
    ]

    await bot.set_my_commands(main_menu_commands)