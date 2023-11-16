import logo from './logo.svg';
import './App.css';
import Nav from './nav';
import Body from './body';
import Footer from './footer';


function Bug(props) {
  const bag = {
    padding: "20px",
    border: "1px solid gray",
    background: "#fff",
    margin: "20px 0"
  }

  return (
    <div style={bag}>
      {props.children}
    </div>
  )
}


function App() {
  return (
    <div>
      <Nav />
      <Body />
      <Footer />
    </div>
  );
}

export default App;