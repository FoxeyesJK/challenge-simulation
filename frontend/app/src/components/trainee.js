import React, { useState, useEffect } from 'react';
import { Header, Dropdown } from 'semantic-ui-react';

const API_URI = 'http://localhost:5000/trainees';

const Trainee = ({handleChange}) => {
    const [trainees, setTrinees] = useState([]);
    
    const getTrainees = async () => {
        const response = await fetch(API_URI);
        const data = await response.json();
        const reformedData = data.reduce((res, cur) => {
            res.push({key: cur.id, text: `${cur.firstName} ${cur.lastName}`, value: cur.id})
            return res;
        }, [])
        setTrinees(reformedData);
    }

    useEffect(() => {
        getTrainees();
    }, [])

    return (
        <div>
            <Header as='h2' content='Trainee' textAlign='center' />
            <p style={{textAlign:'left'}}>
            Please select a trainee:
            </p>
            <Dropdown
                options={trainees}
                placeholder='Select Trainee'
                name='trainee'
                fluid
                search
                selection
                onChange={handleChange}
            />
        </div>
    )
}

export default Trainee;
