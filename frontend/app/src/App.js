import React, { useState } from 'react';

import './App.css';
import 'semantic-ui-css/semantic.min.css'
import { Divider, Grid, Segment, Icon } from 'semantic-ui-react'

import Trainee from './components/trainee';
import Simulation from './components/simulation';

const App = () => {
  const [selectedTraineeId, setSelectedTraineeId] = useState(0);

  const handleTraineeChange = (event, data) => {
    setSelectedTraineeId(data.value);
  }

  return (
    <div className="App">
      <Segment style={{width:'1000px', margin:"150px auto"}}>
        <Grid columns={2} relaxed='very'>
          <Grid.Column>
            <Trainee handleChange={handleTraineeChange} />
          </Grid.Column>
          <Grid.Column>
            {
              !!selectedTraineeId ?
              <Simulation traineeId={selectedTraineeId} /> :
              null
            }
          </Grid.Column>
        </Grid>
        <Divider vertical>
          <Icon name='angle right' />
        </Divider>
      </Segment>
    </div>
  );
}

export default App;
