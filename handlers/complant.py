from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram import Router
from manager_db import Database


complaint_router = Router()
manager_db = Database("complaints.db")


class ComplaintForm(StatesGroup):
    waiting_for_name = State()
    waiting_for_contact = State()
    waiting_for_complaint = State()



@complaint_router.message(Command("complaint"))
async def start_complaint(message: Message, state: FSMContext):
    await message.answer("Пожалуйста, введите ваше имя:")
    await state.set_state(ComplaintForm.waiting_for_name)

@complaint_router.message(ComplaintForm.waiting_for_name)
async def process_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("Введите ваши данные (номер телефона или аккаунт Instagram):")
    await state.set_state(ComplaintForm.waiting_for_contact)

@complaint_router.message(ComplaintForm.waiting_for_contact)
async def process_contact(message: Message, state: FSMContext):
    await state.update_data(contact=message.text)
    await message.answer("Напишите вашу жалобу:")
    await state.set_state(ComplaintForm.waiting_for_complaint)

@complaint_router.message(ComplaintForm.waiting_for_complaint)
async def process_complaint(message: Message, state: FSMContext):
    data = await state.get_data()
    name = data.get("name")
    contact = data.get("contact")
    complaint = message.text.strip()


    manager_db.insert_complaint(name=name, contact=contact, complaint=complaint)


    await message.answer(
        f"Спасибо за вашу жалобу!\n\n"
        f"Имя: {name}\n"
        f"Контакты: {contact}\n"
        f"Жалоба: {complaint}"
    )


    await state.clear()



