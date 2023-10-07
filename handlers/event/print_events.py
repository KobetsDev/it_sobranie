
from aiogram .types import Message
from data.config import EVENT_FORM, HIDE_TITLE
from keyboards.inline.edit import edit_keyboard
from keyboards.inline.event import subscribe_keyboard
from utils.human_datetime import get_datetime, humanize_datetime
from aiogram.utils.markdown import escape_md


async def print_events(message: Message, events: list, edit: bool = False, is_admin: bool = False) -> None:
    """Выводим мероприятия"""
    for event in events:
        title = escape_md(event.get('title'))
        if is_admin and not event.get('status'):
            title = HIDE_TITLE + title

        text = EVENT_FORM.format(
            title,
            escape_md(event.get('text')),
            humanize_datetime(
                get_datetime(
                    event.get('timestamp')
                )
            ),
            event.get('time'),
        )
        reply_markup = edit_keyboard(
            _id=str(event.get('_id')),
            status=event.get('status')) \
            if edit else subscribe_keyboard(
                participants=len(event.get('participants')),  # Кол-во участников
                places=event.get('places'),  # Кол-во мест
                _id=str(event.get('_id')),
                closed=True if len(event.get('participants')) >= event.get('places') else False,  # Если уже нет мест
                iam_participating=True if message.from_user.id in event.get('participants') else False,  # Если пользователь участвует
                is_admin=is_admin
        )
        if event.get('media_type') == 'photo':
            await message.bot.send_photo(message.from_user.id,
                                         event.get('media'),
                                         text,
                                         reply_markup=reply_markup)
        elif event.get('media_type') == 'video':
            await message.bot.send_video(message.from_user.id,
                                         event.get('media'),
                                         caption=text,
                                         reply_markup=reply_markup)


# for event in events:
#         title = event.get('title')
#         if is_admin and not event.get('status'):
#             title = '🚫Скрыто🚫   ' + title

#         text = EVENT_FORM.format(
#             title,
#             event.get('text'),
#             humanize_datetime(
#                 get_datetime(
#                     event.get('timestamp')
#                 )
#             ),
#             event.get('time'),
#         )
#         reply_markup = edit_keyboard(_id=str(event.get('_id')), status=event.get('status'), order=event.get('order_path')) \
#             if edit else subscribe_keyboard(
#                 participants=len(event.get('participants')),  # Кол-во участников
#                 places=event.get('places'),  # Кол-во мест
#                 _id=str(event.get('_id')),
#                 closed=True if len(event.get('participants')) >= event.get('places') else False,  # Если уже нет мест
#                 iam_participating=True if message.from_user.id in event.get('participants') else False,  # Если пользователь участвует
#                 order=event.get('order_path')
#         )
#         if event.get('media_type') == 'photo':
#             if len(event.get('media')) == 1:
#                 await message.bot.send_photo(message.from_user.id,
#                                              event.get('media')[0],
#                                              text,
#                                              reply_markup=reply_markup)
#             else:
#                 # Создать медиа группу
#                 media = types.MediaGroup()
#                 for media_file in event.get('media')[:-1]:
#                     media.attach_photo(media_file)

#                 media.attach_photo(event.get('media')[-1], caption=text)
#                 await message.bot.send_media_group(chat_id=message.chat.id, media=media,
#                                                    #     reply_markup=reply_markup
#                                                    )
#         elif event.get('media_type') == 'video':
#             if len(event.get('media')) == 1:
#                 await message.bot.send_video(message.from_user.id,
#                                              event.get('media')[0],
#                                              caption=text,
#                                              reply_markup=reply_markup)
#             else:
#                 media = types.MediaGroup()
#                 for media_file in event.get('media')[:-1]:
#                     media.attach_video(media_file)

#                 media.attach_video(event.get('media')[-1], caption=text)
#                 await message.bot.send_media_group(chat_id=message.chat.id, media=media)
