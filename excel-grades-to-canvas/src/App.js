// import logo from "./logo.svg";
import logo from "./OIG.jpeg"
import "./App.css";
import Button from '@mui/material/Button';


function App() {
  const handleFileUpload = (event) => {
    console.log("File upload");
  };

  const handleLogin = (event) => {
    // handle login logic here
  };

  return (
    <div className="App">
      <header className="App-header">
        
        <h1>CPSC 121 : Excel Grades to Canvas <span style={text: '8'}>Aprameya Aithal</span> </h1>
      <Button onClick={handleLogin}>Log In</Button>
        <img src={logo} className="App-logo" alt="logo" />
        <p>Upload Excel File</p>
        <Button variant="contained" onClick={handleFileUpload} component="label">
          Choose File
          <input type="file" hidden />
        </Button>
      </header>
    </div>
  );
}

export default App;
