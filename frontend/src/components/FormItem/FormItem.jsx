import styles from './FormItem.module.scss';

function FormItem({ placeholder, type, name }) {
	return (
		<div className={styles.container}>
			<input name={name} type={type} placeholder={placeholder} className={styles.input} />
		</div>
	);
}

export default FormItem;
