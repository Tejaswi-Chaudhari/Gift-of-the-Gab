import {React, useState} from "react";
import {Nav, Modal} from 'react-bootstrap';
import Button from 'react-bootstrap/Button';
import "./Card.css";
import { useHistory } from "react-router-dom";
import { LinkContainer } from "react-router-bootstrap";

const Card=({card, details})  => {
  let history = useHistory();
  const redirect = () => history.push("/signin");
  const [show, setShow] = useState(false); 
  const handleClose = () => setShow(false);
  const handleShow = () => setShow(true);
  var refresh_token=localStorage.getItem('refresh')
  if(refresh_token!=null)
  {
    return(<>
          <div className="col-md-4 col-10 mx-auto container">
            <div class="card" >
              <img src={`http://127.0.0.1:8000${card.thumbnail}`} class="card-img-top" alt="..."/>
              <div class="card-body">
                <h5 class="card-title ">{card.exercise_name}</h5>
                <hr></hr>
                <p class="card-text">{card.description}</p>
                <LinkContainer to={`audioinput/${card.id}`}>
                    <Nav.Link className="rd_activity"><Button variant="primary" className="b_activity">Start Practice</Button></Nav.Link>
                </LinkContainer>
              </div>
            </div>
          </div>
        </>
    )
  }
  else
  {
    return(<>
        <Modal show={show} onHide={handleClose}>
                
                <Modal.Header >
                  <Modal.Title>Please Sign in!
                  </Modal.Title>
                  </Modal.Header>
                <Modal.Body>Sign in to continue</Modal.Body>
                    <Modal.Footer>
                        <LinkContainer to="/signin">
                        <Nav.Link className="link-signin" ><Button variant="primary" >
                            Sign in
                        </Button></Nav.Link>
                        </LinkContainer>
                    </Modal.Footer>
            </Modal>

        <div className="col-md-4 col-10 mx-auto container">
          <div class="card" >
          <img src={`http://127.0.0.1:8000${card.thumbnail}`} class="card-img-top" alt="..."/>
          <div class="card-body">
            <h5 class="card-title ">{card.exercise_name}</h5>
            <hr></hr>
            <p class="card-text">{card.description}</p>
              <Button variant="primary" onClick={handleShow} className="b_activity">Start Practice</Button>
                
                
          </div>
        </div>
      </div>

    </>
  )
  }
}
export default Card
