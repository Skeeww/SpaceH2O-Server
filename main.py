import asyncio, integrity, colored

async def run_integrity():
    if integrity.checknetwork():
        print(colored.stylize("[OK]", colored.fg("green")) + " Network Connection")
    else:
        print(colored.stylize("[ERROR]", colored.fg("red")) + " Network Connection")
    if integrity.checkpusher():
        print(colored.stylize("[OK]", colored.fg("green")) + " Pusher Connection")
    else:
        print(colored.stylize("[ERROR]", colored.fg("red")) + " Pusher Connection")
    if integrity.checkmongo():
        print(colored.stylize("[OK]", colored.fg("green")) + " MongoDB Connection")
    else:
        print(colored.stylize("[ERROR]", colored.fg("red")) + " MongoDB Connection")
    if integrity.checkprocessor():
        print(colored.stylize("[OK]", colored.fg("green")) + " Processor is under 80%")
    else:
        print(colored.stylize("[WARNING]", colored.fg("orange_4a")) + " Processor is upper 80%")
    if integrity.checkram():
        print(colored.stylize("[OK]", colored.fg("green")) + " Ram is under 80%")
    else:
        print(colored.stylize("[WARNING]", colored.fg("orange_4a")) + " Ram is upper 80%")

async def test_thread():
    print("Hey I'm the test thread !")
    await asyncio.sleep(1)

async def run_threads():
    thread_runintegrity = asyncio.create_task(run_integrity())
    await thread_runintegrity
    thread_runintegrity = asyncio.create_task(test_thread())
    await thread_runintegrity

if __name__ == "__main__":
    asyncio.run(run_threads())