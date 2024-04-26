import { useState } from 'react';
import { useForm } from 'react-hook-form';

import cn from 'classnames';
import styles from './NewCoffeeshop.module.scss';
import CheckBox from '../../assets/ui-kit/CheckBox/CheckBox';
import Button from '../../assets/ui-kit/Button/Button';
import CloseButton from '../../assets/ui-kit/CloseButton/CloseButton';

import { BASE_TAGS, SPECIAL_EXTRAS } from '../../utils/constants';

function NewCoffeeshop({ onClose }) {
	const [showPopupCoffeeTypes, setShowPopupCoffeeTypes] = useState(false);
	const [showPopupAlternatives, setShowPopupAlternatives] = useState(false);
	const [textHidden, setTextHidden] = useState(true);
	const inputTimeClassName = cn(styles.input_item, styles.input_medium);

	const handleInputClick = () => {
		setTextHidden(false);
	};

	const handleInputCoffee = () => {
		setShowPopupCoffeeTypes(!showPopupCoffeeTypes);
	};

	const handleCheckboxChange = () => {
		setShowPopupAlternatives(!showPopupAlternatives);
	};

	return (
		<section className={styles.container}>
			<div className={styles.close}>
				<CloseButton onClick={onClose} size="default" />
			</div>
			<form className={styles.container_main}>
				<ul className={styles.input_list}>
					<li className={styles.input_container}>
						<label htmlFor="cafe_name" className={styles.input_label}>
							Название кофейни
						</label>
						<input type="text" id="cafe_name" className={styles.input_item} placeholder="" />
					</li>
					<li className={styles.input_container}>
						<label htmlFor="cafe_name" className={styles.input_label}>
							Адрес
						</label>
						<input type="text" id="cafe_name" className={styles.input_item} placeholder="" />
					</li>
					<li className={styles.input_container}>
						<div className={styles.input_aligner_row}>
							<label htmlFor="cafe_schedule" className={styles.input_label}>
								Пн- Пт
							</label>
							<div>
								<input
									type="text"
									id="cafe_schedule"
									className={inputTimeClassName}
									placeholder="00:00"
								/>
								<input
									type="text"
									id="cafe_schedule"
									className={inputTimeClassName}
									placeholder="00:00"
								/>
							</div>
						</div>
					</li>
					<li className={styles.input_container}>
						<div className={styles.input_aligner_row}>
							<label htmlFor="cafe_schedule" className={styles.input_label}>
								Сб - Вс
							</label>
							<div className={styles.input_aligner}>
								<div style={{ marginBottom: '18px' }}>
									<input
										type="text"
										id="cafe_schedule"
										className={inputTimeClassName}
										placeholder="00:00"
									/>
									<input
										type="text"
										id="cafe_schedule"
										className={inputTimeClassName}
										placeholder="00:00"
									/>
								</div>
								<CheckBox text="Как в будни" />
								<CheckBox text="Круглосуточно" />
							</div>
						</div>
					</li>
					<li className={styles.input_container} style={{ flexDirection: 'column' }}>
						<div className={styles.input_aligner_row} style={{ justifyContent: 'flex-start' }}>
							<label htmlFor="cafe_drink" className={styles.input_label}>
								Напитки
							</label>
							<div className={styles.input_aligner} style={{ flexDirection: 'row' }}>
								<input type="text" id="cafe_drink" className={inputTimeClassName} placeholder="" />
								<input
									type="text"
									id="cafe_drink"
									className={inputTimeClassName}
									style={{ width: '76px' }}
									placeholder=""
								/>
							</div>
						</div>
						<p className={styles.input_add}>+ добавить напиток</p>
					</li>
					<li className={styles.input_container}>
						<div className={styles.input_aligner_row} style={{ justifyContent: 'flex-start' }}>
							<label htmlFor="cafe_tags" className={styles.input_label}>
								Доступные опции
							</label>
							<div className={styles.input_aligner}>
								<div>
									{BASE_TAGS.map(item => (
										<CheckBox key={item.id} text={item.text} />
									))}
								</div>
							</div>
						</div>
					</li>

					<li className={styles.input_container}>
						<label htmlFor="cafe_roasters" className={styles.input_label}>
							Обжарщики
						</label>
						<div>
							<input type="text" id="cafe_roasters" className={styles.input_item} />
							<p className={styles.input_add}>+ добавить обжарщика</p>
						</div>
					</li>

					<li className={styles.input_container}>
						<div className={styles.input_aligner_row} style={{ justifyContent: 'flex-start' }}>
							<label htmlFor="cafe_schedule" className={styles.input_label}>
								Доступные опции
							</label>
							<div className={styles.input_aligner}>
								<div>
									{SPECIAL_EXTRAS.map(item => (
										<CheckBox key={item.id} text={item.text} />
									))}
								</div>
							</div>
						</div>
					</li>

					<li className={styles.input_container}>
						<label htmlFor="cafe_description" className={styles.input_label}>
							Описание
						</label>
						<textarea
							type="text"
							id="cafe_description"
							className={styles.input_item}
							style={{ height: '128px' }}
						/>
					</li>

					<li className={styles.input_container}>
						<label htmlFor="cafe_image" className={styles.input_label}>
							Фото на обложку
						</label>
						<textarea
							type="text"
							id="cafe_image"
							className={styles.input_item}
							style={{
								height: '128px',
								background: 'rgba(145, 224, 200, 0.2)',
								boxShadow: 'var(--box-shadow)',
							}}
							placeholder="Выберите файл или перетащите его сюда"
						/>
					</li>
				</ul>
				<Button text="Добавить кофейню" type="submit" size="medium" />
			</form>
		</section>
	);
}

export default NewCoffeeshop;
