import './sass/main.scss'

import React, { Component } from 'react';
import ReactDOM from 'react-dom';

class SnapburgCarousel extends Component {
    render() {
        return (
            <div>
                <div>
                    <img src="/assets/mis.jpeg" />
                    <p className="legend">Legend 1</p>
                </div>
                <div>
                    <img src="/assets/pace.jpeg" />
                    <p className="legend">Legend 2</p>
                </div>
                <div>
                    <img src="/assets/vinci.jpeg" />
                    <p className="legend">Legend 3</p>
                </div>
            </div>
        );
    }
};

ReactDOM.render(<SnapburgCarousel />, document.querySelector('#root'));


