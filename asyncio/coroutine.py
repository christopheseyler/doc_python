import asyncio

async def fetch_data(delay, id):
	print("Fetching data... id:", id)
	await asyncio.sleep(delay) # simulate an I/O operation
	print("Data Fetched , id:", id)
	return {"data":"some data", "id":id} # Return some data


async def main():
	task1 = fetch_data(2, 1)
	task2 = fetch_data(3, 2)
	
	result1 = await task1
	print(f"Received result: {result1}")
	
	result2 = await task2
	print(f"Received result: {result2}")
		
# Run the main coroutine
asyncio.run(main())


