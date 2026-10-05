import { useState } from "react";

function App() {
    const [message, setMessage] = useState("");

    async function checkAuthService() {
        try {
            const response = await fetch(
                "http://127.0.0.1:8001/api/health/"
            );

            const data = await response.json();

            setMessage(
                `${data.service}: ${data.status}`
            );
        } catch (error) {
            setMessage("Auth service is unavailable");
        }
    }

    async function checkBillService() {
        try {
            const response = await fetch(
                "http://127.0.0.1:8002/api/health/"
            );

            const data = await response.json();

            setMessage(
                `${data.service}: ${data.status}`
            );
        } catch (error) {
            setMessage("Bill service is unavailable");
        }
    }

    return (
        <div>
            <h1>Microservices Demo</h1>

            <button onClick={checkAuthService}>
                Check Auth Service
            </button>

            <button onClick={checkBillService}>
                Check Bill Service
            </button>

            <p>{message}</p>
        </div>
    );
}

export default App;