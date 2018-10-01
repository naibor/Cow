import React, { Component } from 'react';
import './App.css'

class SignUp extends Component{
  render(){
    return <form className="signupForm form-horizontal">
        <div>
          <h3>Sign Up</h3>
        </div>
        <div className="form-group">
          <label for="username">Name</label>
          <input type="text" name="name" className="form-control" placeholder="Enter Name" required />
        </div>
        <div className="form-group">
          <label for="username">Email</label>
          <input type="email" name="email" className="form-control" placeholder="Email" required />
        </div>
        <div className="form-group">
          <label for="username">Password</label>
          <input type="password" name="password" className="form-control" placeholder="Desired password" required />
        </div>
        <div className="form-group">
          <label for="username">Confirm Password</label>
          <input type="password" name="confirmPassword" className="form-control" placeholder="Confirm password" required />
        </div>
        <div>
          <input value="Sign Up" type="submit" className="btn btn-success" />
        </div>
      </form>;
        }
}
class NavBar extends Component{
  render(){
    return (
            <nav className="navbar navbar-expand-lg bg-dark">
                <a className="navbar-brand" href="">
                  Cow
                </a>
                <button className="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                  <span className="navbar-toggler-icon" />
                </button>
                <div className="collapse navbar-collapse" id="navbarContent">
                  <ul className="navbar-nav ml-auto">
                    <li className="nav-item">
                      <a className="nav-link " href="">About Us</a>
                    </li>
                    <li className="nav-item">
                      <input type="button" className="btn btn-success" value="LOG IN"></input>
                    </li>
                  </ul>
                </div>
              </nav>
      );
  }
}
class App extends Component {
  render() {
    return(
      <div>
        <NavBar />
        <div className="container-fluid">
          <div className="row">
            <div className="col-xs-4 content">
              <SignUp />
            </div>
          </div>
        </div>
      </div>
      );
  }
}

export default App ;
