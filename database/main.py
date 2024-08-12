import sys
from modules import mod
import asyncio
from asyncio import Runner

if __name__ == "__main__":
    if len(sys.argv) > 1:
        if ".xls" in sys.argv[1]:
            asyncio.run(mod.insert_question_to_db(sys.argv[1]))
        elif "delquestions" in sys.argv[1]:
            asyncio.run(mod.clear_questions_to_db())
        elif "delquestion" in sys.argv[1]:
            asyncio.run(mod.clear_question_to_db())
        elif "delall" in sys.argv[1]:
            with Runner() as runner:
                runner.run(mod.clear_question_to_db())
                runner.run(mod.clear_questions_to_db())
                runner.run(mod.clear_users_to_db())