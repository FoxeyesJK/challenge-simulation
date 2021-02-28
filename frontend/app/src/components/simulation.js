import React, { useState, useEffect } from 'react';
import { Header, Dropdown, Button } from 'semantic-ui-react';

const API_URI = 'http://localhost:5000';

const Simulation = ({traineeId}) => {
    const [simulations, setSimulations] = useState([]);
    const [selectedSimulations, setSelectedSimulations] = useState([]);
    const [client, setClient] = useState({});
    const [message, setMessage] = useState('');
    
    const getSimulations = async () => {
        const response = await fetch(`${API_URI}/simulations`);
        const data = await response.json();
        const reformedData = data.reduce((res, cur) => {
            res.push({key: cur.id, text: cur.name, value: cur.id })
            return res;
        }, [])
        setSimulations(reformedData);
    }

    const getTraineeClient = async () => {
        const response = await fetch(`${API_URI}/clients?traineeId=${traineeId}`);
        const data = await response.json();
        setClient(data);
    }

    const getTraineeSimulations = async () => {
        const response = await fetch(`${API_URI}/simulations?traineeId=${traineeId}`);
        const data = await response.json();
        const reformedData = data.map(a => a.id);
        setSelectedSimulations(reformedData);
    }

    const postClientSimulationMapping = async () => {
        const reformedData = {
            clientId: client.id, 
            simulationIds: selectedSimulations
        }
        
        console.log(reformedData);

        const requestOptions = {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(reformedData)
        }

        const response = await fetch(`${API_URI}/client-simulation-mapping`, requestOptions);
        const data = await response.status;

        if (data === 201)
            setMessage('Successfully updated');
        else
            setMessage('Failed to update simulations. Try again!')
    }

    const handleChange = (event, data) => {
        setSelectedSimulations(data.value);
    }
    
    const handleClick = () => {
        postClientSimulationMapping();
    }

    useEffect(() => {
        getSimulations();
        getTraineeClient();
        getTraineeSimulations();
        setMessage('');
    }, [traineeId])

    return (
        <div>
            <Header as='h2' content='Simulation' textAlign='center' />
            {
                client ? 
                <div>
                    <span style={{fontWeight:'bold'}}>Client: </span>
                    {client.name} ({client.code})
                </div> :
                null 
            }
            <p style={{textAlign:'left'}}>
                Please select simulations:
            </p>
            <div>
                <Dropdown
                    placeholder='Simulation'
                    fluid
                    multiple
                    search
                    selection
                    value={selectedSimulations}
                    onChange={handleChange}
                    options={simulations}
                />
                <div style={{color:'red',textAlign:'left'}}>{message}</div>
                <Button primary style={{margin:'20px'}} onClick={handleClick}>Save</Button>
            </div>
        </div>
    )
}

export default Simulation;