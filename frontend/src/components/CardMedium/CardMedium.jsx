import { useSelector } from 'react-redux';
import { useLocation } from 'react-router-dom';
import { Map, Placemark } from '@pbe/react-yandex-maps';

import cn from 'classnames';
import styles from './CardMedium.module.scss';

import BackButton from '../../assets/ui-kit/BackButton/BackButton';
import FavouritesButton from '../../assets/ui-kit/FavouritesButton/FavouritesButton';
import nullImage from '../../assets/images/logo.svg';

import { useGetCardByIdQuery } from '../../slices/apiSlice/apiSlice';

import locationImg from '../../assets/images/location-pin.svg';

function CardMedium() {
	const location = useLocation();
	const theme = useSelector(state => state.theme);
	const { data, isLoading } = useGetCardByIdQuery(location.state.key);

	if (isLoading) {
		return <p>LOADING....</p>;
	}

	const {
		address,
		alternatives,
		availables,
		description,
		id,
		image,
		name,
		roasters,
		schedules,
		additionals,
		drinks,
	} = data;

	const imgClassName = cn(styles.img, { [styles.img_null]: !image });

	return (
		<section className={styles.container}>
			<BackButton type="button" theme={theme} text="Назад" />

			<div className={styles.heading}>
				<div className={styles.title}>
					<h1>{name}</h1>
					<p>{description}</p>
				</div>
				<div className={styles.map}>
					<div className={styles.map_mini}>
						<Map
							defaultState={{ center: [address.lat, address.lon], zoom: 11 }}
							width="inherit"
							height="inherit"
							modules={['geoObject.addon.balloon', 'geoObject.addon.hint']}
							options={{ exitFullscreenByEsc: true, yandexMapDisablePoiInteractivity: true }}
						>
							<Placemark
								geometry={[address.lat, address.lon]}
								options={{
									preset: 'islands#circleIcon',
									iconLayout: 'default#image',
									iconImageHref: locationImg,
									iconImageSize: [30, 30],
									hideIconOnBalloonOpen: false,
									balloonCloseButton: false,
								}}
							/>
						</Map>
					</div>
					<button className={styles.button} type="button">
						Построить маршрут
					</button>
				</div>
				<div className={styles.info}>
					<div className={styles.info_container}>
						<div className={theme === 'light' ? styles.point_icon : styles.point_icon_dark} />
						<p>{address.name}</p>
					</div>
					<div className={styles.info_container}>
						<div className={theme === 'light' ? styles.schedule_icon : styles.schedule_icon_dark} />
						<ul className={styles.schedules}>
							{schedules.map(item => (
								<li key={item.id} className={styles.schedules_item}>
									<p> {item.name}</p>
									<p> {item.start.slice(0, -3)}</p>
									<p> {item.end.slice(0, -3)}</p>
								</li>
							))}
						</ul>
					</div>
				</div>
			</div>
			<div className={styles.desription}>
				<div className={styles.photo}>
					<img className={imgClassName} src={!image ? nullImage : image} alt="фото кофейни" />
					<div className={styles.favourites}>
						{' '}
						<FavouritesButton type="button" card={data} />
					</div>
				</div>
				<div className={styles.features}>
					<h3 className={cn(styles.tag1, styles.tag)}>Доступно</h3>
					<ul className={cn(styles.list1, styles.list)}>
						{availables.map(item => (
							<li key={item.id}>{item.name}</li>
						))}
					</ul>

					<h3 className={cn(styles.tag2, styles.tag)}>Напитки</h3>
					<div className={cn(styles.list2)}>
						<ul className={cn(styles.list)}>
							{drinks.map(item => (
								<li key={item.id}>{`${item.name}: ${item.cost} ₽`} </li>
							))}
						</ul>
					</div>

					<h3 className={cn(styles.tag3, styles.tag)}>Обжарщик</h3>
					<ul className={cn(styles.list3, styles.list)}>
						{roasters.map(item => (
							<li key={item.id}>{item.name}</li>
						))}
					</ul>
					<h3 className={cn(styles.tag4, styles.tag)}>Альтернатива</h3>
					<div className={cn(styles.list4, styles.list)}>
						{alternatives.map(item => (
							<li key={item.id}>{item.name}</li>
						))}
					</div>
					<h3 className={cn(styles.tag5, styles.tag)}>Дополнительно</h3>
					<ul className={cn(styles.list5, styles.list)}>
						{additionals.map(item => (
							<li key={item.id}>{item.name}</li>
						))}
					</ul>
				</div>
			</div>
		</section>
	);
}

export default CardMedium;
