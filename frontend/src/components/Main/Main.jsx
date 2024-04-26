import styles from './Main.module.scss';

import TagSection from '../TagSection/TagSection';
import MainSection from '../MainSection/MainSection';

function Main() {
	return (
		<main className={styles.main}>
			<TagSection />
			<MainSection />
		</main>
	);
}

export default Main;
