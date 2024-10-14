from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = '7308319429:AAEi8oV9SEIcYmgVwkBdHqYwAJgFRDwDp0Q'

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Привет! Я графический редактор. Введите команды для построения графических примитивов.')

async def handle_line(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    args = context.args
    if len(args) != 4:
        await update.message.reply_text('Использование: /line x1 y1 x2 y2')
        return
    try:
        x1, y1, x2, y2 = map(int, args)
        command = f'plt.plot([{x1}, {x2}], [{y1}, {y2}])'
        await update.message.reply_text(f'Команда для построения линии: {command}')
    except ValueError:
        await update.message.reply_text('Все координаты должны быть числами.')

async def handle_rectangle(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    args = context.args
    if len(args) != 2:
        await update.message.reply_text('Использование: /rectangle width height')
        return
    try:
        width, height = map(int, args)
        command = f'plt.gca().add_patch(plt.Rectangle((0, 0), {width}, {height}))'
        await update.message.reply_text(f'Команда для построения прямоугольника: {command}')
    except ValueError:
        await update.message.reply_text('Ширина и высота должны быть числами.')

async def handle_circle(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    args = context.args
    if len(args) != 3:
        await update.message.reply_text('Использование: /circle x y radius')
        return
    try:
        x, y, radius = map(int, args)
        command = f'plt.gca().add_patch(plt.Circle(({x}, {y}), {radius}))'
        await update.message.reply_text(f'Команда для построения круга: {command}')
    except ValueError:
        await update.message.reply_text('Все параметры должны быть числами.')

async def handle_ellipse(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    args = context.args
    if len(args) != 4:
        await update.message.reply_text('Использование: /ellipse x y width height')
        return
    try:
        x, y, width, height = map(int, args)
        command = f'plt.gca().add_patch(plt.Ellipse(({x}, {y}), {width}, {height}))'
        await update.message.reply_text(f'Команда для построения эллипса: {command}')
    except ValueError:
        await update.message.reply_text('Все параметры должны быть числами.')

async def handle_point(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    args = context.args
    if len(args) != 2:
        await update.message.reply_text('Использование: /point x y')
        return
    try:
        x, y = map(int, args)
        command = f'plt.plot({x}, {y}, "o")'
        await update.message.reply_text(f'Команда для построения точки: {command}')
    except ValueError:
        await update.message.reply_text('Координаты должны быть числами.')

async def handle_triangle(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    args = context.args
    if len(args) != 6:
        await update.message.reply_text('Использование: /triangle x1 y1 x2 y2 x3 y3')
        return
    try:
        x1, y1, x2, y2, x3, y3 = map(int, args)
        command = f'plt.gca().add_patch(plt.Polygon(([{x1}, {y1}], [{x2}, {y2}], [{x3}, {y3}]), closed=True))'
        await update.message.reply_text(f'Команда для построения треугольника: {command}')
    except ValueError:
        await update.message.reply_text('Все координаты должны быть числами.')

async def handle_polygon(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    args = context.args
    if len(args) % 2 != 0 or len(args) < 6:
        await update.message.reply_text('Использование: /polygon x1 y1 x2 y2 x3 y3 ...')
        return
    try:
        points = [tuple(map(int, args[i:i + 2])) for i in range(0, len(args), 2)]
        command = f'plt.gca().add_patch(plt.Polygon({points}, closed=True))'
        await update.message.reply_text(f'Команда для построения многоугольника: {command}')
    except ValueError:
        await update.message.reply_text('Все координаты должны быть числами.')

async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    args = context.args
    if len(args) < 3:
        await update.message.reply_text('Использование: /text x y "текст"')
        return
    try:
        x, y = map(int, args[:2])
        text = ' '.join(args[2:])
        command = f'plt.text({x}, {y}, "{text}")'
        await update.message.reply_text(f'Команда для добавления текста: {command}')
    except ValueError:
        await update.message.reply_text('Координаты должны быть числами.')

def main() -> None:
    application = ApplicationBuilder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("line", handle_line))
    application.add_handler(CommandHandler("rectangle", handle_rectangle))
    application.add_handler(CommandHandler("circle", handle_circle))
    application.add_handler(CommandHandler("ellipse", handle_ellipse))
    application.add_handler(CommandHandler("point", handle_point))
    application.add_handler(CommandHandler("triangle", handle_triangle))
    application.add_handler(CommandHandler("polygon", handle_polygon))
    application.add_handler(CommandHandler("text", handle_text))

    application.run_polling()

if __name__ == '__main__':
    main()
