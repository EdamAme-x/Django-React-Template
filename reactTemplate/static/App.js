function App() {
    return <>
        <h1>Hello Django & React!</h1>
        <div>
            <img src="/static/React.svg" alt="react" width="200" />
            <img src="/static/Django.svg" alt="react" width="200" />
        </div>
    </>
}

const root = ReactDOM.createRoot(document.getElementById('app'));
root.render(
    <React.StrictMode>
        <App />
    </React.StrictMode>
);