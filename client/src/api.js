export const fetchResponse =  async(chat) => {
    try {
        // after depoloyment you should change the fetch URL below
        const response = await fetch("https://grammarasticapi.onrender.com/correct", { 
            method: 'POST',
            headers: {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "http://127.0.0.1:5173",
                "Access-Control-Allow-Origin": "https://frontend-grammarastic.vercel.app/"
            },
            body: JSON.stringify({
                message: chat.message
            })
        })

        const data = await response.json()
        return data

    } catch (error) {
        console.log(error);
    }
}
