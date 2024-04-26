import { NavLink } from 'react-router-dom';
import styles from './Footer.module.scss';

import HorizontalLine from '../HorizontalLine/HorizontalLine';

function Footer() {
	return (
		<>
			<HorizontalLine />
			<footer className={styles.footer}>
				<div className={styles.container}>
					<div className={styles.text}>
						<h3>Сделано студентами Яндекс Практикума</h3>
						<p>
							Icons made by Vectorstall, Ade Nur Hidayat, Kmg Design from{' '}
							<a href="https://thenounproject.com/" className={styles.link_icons}>
								thenounproject.com
							</a>{' '}
						</p>
					</div>

					<div className={styles.aligner}>
						<NavLink to="/signin" className={styles.link_profile}>
							<h3>Coffeeguide PRO</h3>
						</NavLink>
						<h3>&copy;Copyright 2024 CoffeeGuide</h3>
					</div>
				</div>
			</footer>
		</>
	);
}

export default Footer;
