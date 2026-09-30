import React, { useState } from 'react';

const GEDCOMParser = () => {
    const [data, setData] = useState();

    const parseGEDCOM = (gedcomData) => {
        let parsedData = {};
        gedcomData.split("\n").forEach(line => {
            let fields = line.split(" ");
            parsedData[fields[1]] = fields[2]
        });
        setData(parsedData);
    }

    return (
        <React.Fragment>
            <input
                type="file"
                accept=".ged"
                onChange={({ target }) => parseGEDCOM(target.file)}
            />
            {data && (
                <div>
                    {Object.keys(data).map(key => (
                        <div key={key}>{key}: {data[key]}</div>
                    ))}
                </div>
            )}
        </React.Fragment>
    );
};

export default GEDCOMParser;