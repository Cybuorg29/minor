import React from 'react';

const ListView = (props) => {
    return (
        <div>
            {
                props.items.map((item, index) => (
                    <li key={index}>{item}</li>
                ))
            }
        </div>
    );
}

export default ListView;