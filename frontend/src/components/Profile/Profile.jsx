import { useState } from 'react';
import styles from './Profile.module.scss';

import Button from '../../assets/ui-kit/Button/Button';
import CardSmall from '../CardSmall/CardSmall';
import NewCoffeeshop from '../NewCoffeeshop/NewCoffeeshop';

function Profile() {
	const [isOpen, setIsOpen] = useState(false);
	return isOpen ? (
		<NewCoffeeshop onClose={() => setIsOpen(false)} />
	) : (
		<section className={styles.container}>
			<div className={styles.button_container}>
				<Button
					type="button"
					size="medium"
					text="добавить кофейню"
					onClick={() => setIsOpen(true)}
				/>
			</div>
			<div className={styles.content}>
				{/* <ul className={styles.grid}>
					{cards.map(item => (
						<li key={item.id}>
							<CardSmall card={item} />
						</li>
					))}
				</ul> */}
				<p className={styles.text}>
					Добро пожаловать в COFFEE GUIDE! У вас пока нет добавленных кофеен. Если ваша кофейня уже
					есть на сайте свяжитесь с нами admin@gmail.com
				</p>
			</div>
		</section>
	);
}

export default Profile;
