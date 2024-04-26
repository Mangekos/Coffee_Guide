import React, { useState, useEffect } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { Map, Placemark, FullscreenControl } from '@pbe/react-yandex-maps';
import cn from 'classnames';

import { useGetCardsQuery } from '../../slices/apiSlice/apiSlice';

import BalloonModal from '../BalloonModal/BalloonModal';
import CardSmall from '../CardSmall/CardSmall';

import styles from './MapComponent.module.scss';
import location from '../../assets/images/location-pin.svg';

function MapComponent() {
	const [isActive, setIsActive] = useState(false);
	const [isCard, setIsCard] = useState({});
	const [place, setPlace] = useState({});
	const card = useSelector(state => state.cards.cards);

	const handleOpenBalloon = () => {
		setIsActive(true);
	};

	const handleCloseBalloon = () => {
		setIsActive(false);
		place.balloon.close();
	};

	return (
		<div className={styles.container}>
			<Map
				defaultState={{ center: [55.75, 37.57], zoom: 11 }}
				width="inherit"
				height="inherit"
				modules={['geoObject.addon.balloon', 'geoObject.addon.hint']}
				options={{ exitFullscreenByEsc: true, yandexMapDisablePoiInteractivity: true }}
				instanceRef={setPlace}
				onClick={handleCloseBalloon}
			>
				{card?.map(card => (
					<Placemark
						key={card.id}
						geometry={[card.address.lat, card.address.lon]}
						options={{
							preset: 'islands#circleIcon',
							iconLayout: 'default#image',
							iconImageHref: location,
							iconImageSize: [30, 30],
							hideIconOnBalloonOpen: false,
							balloonCloseButton: false,
						}}
						properties={{
							balloonContent: `<div id="balloon-comp" class=${styles.map_hint} ></div>`,
						}}
						onClick={() => {
							setTimeout(() => {
								handleOpenBalloon();
								setIsCard(card);
							}, 0);
						}}
					/>
				))}
				<FullscreenControl options={{ visible: true }} data={{ content: '<p>BLABLABLA</p>' }} />
			</Map>
			{isActive && (
				<BalloonModal elementId="balloon-comp">
					<CardSmall card={isCard} />
				</BalloonModal>
			)}
		</div>
	);
}

export default MapComponent;
