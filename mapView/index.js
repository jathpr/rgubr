{/*import React from 'react';
import { render } from 'react-dom';
import Root from './root'; // import Root that we just created

// rendering the Root component into <div id="App"></div>
render(
  <Root />,
  document.getElementById('App')
);*/}
import React from 'react';
import { render } from 'react-dom';
import { Map, Marker, Popup, TileLayer } from 'react-leaflet';

const position = [52.0943, 23.705];
const map = (
  <Map center={position} zoom={13}>
    <TileLayer
      url='http://{s}.tile.osm.org/{z}/{x}/{y}.png'
      attribution='&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
    />
    <Marker position={position}>
      <Popup>
        <span>A pretty CSS3 popup.<br/>Easily customizable.</span>
      </Popup>
    </Marker>
  </Map>
);

render(map, document.getElementById('App'));
