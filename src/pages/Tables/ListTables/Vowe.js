import React from "react";
import { Card, CardBody, Col, Container, Row } from "reactstrap";

import Data from "../../../Components/Common/Data";

const Vowe = () => {
  document.title = "Listjs | Velzon - React Admin & Dashboard Template";

  return (
    <React.Fragment>
        <Container fluid>
          <Row>
            <Col lg={12}>
              <Card>
                <CardBody>
                  <Data />
                </CardBody>
              </Card>
            </Col>
          </Row>
        </Container>
    </React.Fragment>
  );
};

export default Vowe;
