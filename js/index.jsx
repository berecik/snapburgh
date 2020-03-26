import './sass/main.scss'

import React, {Component} from 'react';
import ReactDOM from 'react-dom';

class SnapPhoto extends Component {
    render(){
        return <img src={this.props.snap.photo} key={'photo_' + this.props.snap.id} />
    }
}

class SnapThumbnail extends Component {
    render(){
        return <img src={this.props.snap.thumbnail} key={'thumbnail_' + this.props.snap.id} />
    }
}

class SnapSlide extends Component {
    render(){
        return <div className="slide" style={{
            backgroundImage: `url(${this.props.snap.photo})`
        }}/>
    }
}

class SnapburgCarousel extends Component {
    render() {
        const gallery = window.gallery;
        const snaps = gallery.snaps;
        const photos = snaps.map(snap => <SnapPhoto snap={snap} key={'photo_' + snap.id} />);
        const thumbnails = snaps.map(snap => <SnapThumbnail snap={snap} key={'thumbnail_' + snap.id} />);
        const slides = snaps.map(snap => <SnapSlide snap={snap} key={'slide_' + snap.id} />);

        return (
            <div>
                <div className="slider">
                    {photos}
                </div>
            </div>
        );
    }
};

ReactDOM.render(<SnapburgCarousel/>, window.react_mount,);
