from .paxModule import buildRequest, apiPaxFunctions
import asyncio
import aiohttp

async def push_command(idList:list, command:str, **kwargs):
    
    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session:
        tasks = [asyncio.create_task(buildRequest(session, "pushCommand", command=command , terminalId = id)) for id in idList]
        responses = await asyncio.gather(*tasks)

        for response in responses:
            print(response)




async def main():
    serialNoList = [1190018310,1190018708,1190018329]
    operation = apiPaxFunctions()
    group = await operation.startPaxGroup(serialNoList)
    command = await push_command(group['id'], 'Restart')

if __name__ == '__main__':
    asyncio.run(main())

    
