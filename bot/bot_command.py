import matplotlib.pyplot as plt
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import io

TOKEN = '7308319429:AAEi8oV9SEIcYmgVwkBdHqYwAJgFRDwDp0Q'

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Привет! Я графический редактор киностудии. Введите команды для построения графических примитивов.')

async def handle_line(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    args = context.args
    if len(args) != 4:
        await update.message.reply_text('Использование: /line x1 y1 x2 y2')
        return
    try:
        x1, y1, x2, y2 = map(int, args)
        fig, ax = plt.subplots()
        ax.plot([x1, x2], [y1, y2])
        ax.set_xlabel('X axis')
        ax.set_ylabel('Y axis')
        ax.set_title('Line Plot')
        ax.grid(True)
        
        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)
        await update.message.reply_photo(buf)
        buf.close()
        plt.close(fig)
    except ValueError:
        await update.message.reply_text('Все координаты должны быть числами.')

async def handle_rectangle(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    args = context.args
    if len(args) != 2:
        await update.message.reply_text('Использование: /rectangle width height')
        return
    try:
        width, height = map(int, args)
        fig, ax = plt.subplots()
        ax.add_patch(plt.Rectangle((0, 0), width, height, fill=None, edgecolor='r'))
        ax.set_xlim(-10, width + 10)
        ax.set_ylim(-10, height + 10)
        ax.set_xlabel('X axis')
        ax.set_ylabel('Y axis')
        ax.set_title('Rectangle')
        ax.grid(True)
        
        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)
        await update.message.reply_photo(buf)
        buf.close()
        plt.close(fig)
    except ValueError:
        await update.message.reply_text('Ширина и высота должны быть числами.')

async def handle_circle(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    args = context.args
    if len(args) != 3:
        await update.message.reply_text('Использование: /circle x y radius')
        return
    try:
        x, y, radius = map(int, args)
        fig, ax = plt.subplots()
        ax.add_patch(plt.Circle((x, y), radius, fill=None, edgecolor='b'))
        ax.set_xlim(x - radius - 10, x + radius + 10)
        ax.set_ylim(y - radius - 10, y + radius + 10)
        ax.set_xlabel('X axis')
        ax.set_ylabel('Y axis')
        ax.set_title('Circle')
        ax.grid(True)
        
        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)
        await update.message.reply_photo(buf)
        buf.close()
        plt.close(fig)
    except ValueError:
        await update.message.reply_text('Все параметры должны быть числами.')

async def handle_ellipse(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    args = context.args
    if len(args) != 4:
        await update.message.reply_text('Использование: /ellipse x y width height')
        return
    try:
        x, y, width, height = map(int, args)
        fig, ax = plt.subplots()
        ax.add_patch(plt.Ellipse((x, y), width, height, fill=None, edgecolor='g'))
        ax.set_xlim(x - width//2 - 10, x + width//2 + 10)
        ax.set_ylim(y - height//2 - 10, y + height//2 + 10)
        ax.set_xlabel('X axis')
        ax.set_ylabel('Y axis')
        ax.set_title('Ellipse')
        ax.grid(True)
        
        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)
        await update.message.reply_photo(buf)
        buf.close()
        plt.close(fig)
    except ValueError:
        await update.message.reply_text('Все параметры должны быть числами.')

async def handle_point(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    args = context.args
    if len(args) != 2:
        await update.message.reply_text('Использование: /point x y')
        return
    try:
        x, y = map(int, args)
        fig, ax = plt.subplots()
        ax.plot(x, y, 'ro')  # 'ro' означает красная точка
        ax.set_xlim(x - 10, x + 10)
        ax.set_ylim(y - 10, y + 10)
        ax.set_xlabel('X axis')
        ax.set_ylabel('Y axis')
        ax.set_title('Point')
        ax.grid(True)
        
        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)
        await update.message.reply_photo(buf)
        buf.close()
        plt.close(fig)
    except ValueError:
        await update.message.reply_text('Координаты должны быть числами.')

async def handle_triangle(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    args = context.args
    if len(args) != 6:
        await update.message.reply_text('Использование: /triangle x1 y1 x2 y2 x3 y3')
        return
    try:
        x1, y1, x2, y2, x3, y3 = map(int, args)
        fig, ax = plt.subplots()
        ax.add_patch(plt.Polygon([[x1, y1], [x2, y2], [x3, y3]], closed=True, fill=None, edgecolor='m'))
        ax.set_xlim(min(x1, x2, x3) - 10, max(x1, x2, x3) + 10)
        ax.set_ylim(min(y1, y2, y3) - 10, max(y1, y2, y3) + 10)
        ax.set_xlabel('X axis')
        ax.set_ylabel('Y axis')
        ax.set_title('Triangle')
        ax.grid(True)
        
        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)
        await update.message.reply_photo(buf)
        buf.close()
        plt.close(fig)
    except ValueError:
        await update.message.reply_text('Все координаты должны быть числами.')

async def handle_polygon(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    args = context.args
    if len(args) % 2 != 0 or len(args) < 6:
        await update.message.reply_text('Использование: /polygon x1 y1 x2 y2 x3 y3 ...')
        return
    try:
        points = [tuple(map(int, args[i:i + 2])) for i in range(0, len(args), 2)]
        fig, ax = plt.subplots()
        ax.add_patch(plt.Polygon(points, closed=True, fill=None, edgecolor='c'))
        xs, ys = zip(*points)
        ax.set_xlim(min(xs) - 10, max(xs) + 10)
        ax.set_ylim(min(ys) - 10, max(ys) + 10)
        ax.set_xlabel('X axis')
        ax.set_ylabel('Y axis')
        ax.set_title('Polygon')
        ax.grid(True)
        
        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)
        await update.message.reply_photo(buf)
        buf.close()
        plt.close(fig)
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
        fig, ax = plt.subplots()
        ax.text(x, y, text)
        ax.set_xlim(x - 10, x + 100)
        ax.set_ylim(y - 10, y + 50)
        ax.set_xlabel('X axis')
        ax.set_ylabel('Y axis')
        ax.set_title('Text')
        ax.grid(True)
        
        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)
        await update.message.reply_photo(buf)
        buf.close()
        plt.close(fig)
    except ValueError:
        await update.message.reply_text('Координаты должны быть числами.')

async def handle_random(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    commands = [
        f'/line {random.randint(0, 100)} {random.randint(0, 100)} {random.randint(0, 100)} {random.randint(0, 100)}',
        f'/rectangle {random.randint(10, 50)} {random.randint(10, 50)}',
        f'/circle {random.randint(0, 100)} {random.randint(0, 100)} {random.randint(5, 20)}',
        f'/ellipse {random.randint(0, 100)} {random.randint(0, 100)} {random.randint(10, 50)} {random.randint(10, 50)}',
        f'/point {random.randint(0, 100)} {random.randint(0, 100)}',
        f'/triangle {random.randint(0, 100)} {random.randint(0, 100)} {random.randint(0, 100)} {random.randint(0, 100)} {random.randint(0, 100)} {random.randint(0, 100)}',
        f'/polygon {random.randint(0, 100)} {random.randint(0, 100)} {random.randint(0, 100)} {random.randint(0, 100)} {random.randint(0, 100)} {random.randint(0, 100)}',
        f'/text {random.randint(0, 100)} {random.randint(0, 100)} "Hello, World!"'
    ]
    command = random.choice(commands)
    await update.message.reply_text(f'Случайная команда: {command}')

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
    application.add_handler(CommandHandler("random", handle_random))

    application.run_polling()

if __name__ == '__main__':
    main()
