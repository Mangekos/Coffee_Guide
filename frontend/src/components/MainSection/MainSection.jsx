import styles from './MainSection.module.scss';

import Cards from '../Cards/Cards';
import MapComponent from '../Map/MapComponent';

function MainSection({ cards, expandList }) {
	return (
		<section className={styles.main}>
			<p className={styles.text}>Подобрали для тебя кофейни</p>
			<div className={styles.container}>
				<Cards cards={cards} expandList={expandList} />
				<MapComponent cards={cards} />
			</div>
		</section>
	);
}

export default MainSection;
