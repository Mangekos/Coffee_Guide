import { useEffect } from 'react';
import { createPortal } from 'react-dom';

function BalloonModal({ children, elementId }) {
	const mount = document.getElementById(elementId);
	const el = document.createElement('div');

	useEffect(() => {
		if (mount) mount.appendChild(el);
		return () => {
			if (mount) mount.removeChild(el);
		};
	}, [el, mount]);

	if (!mount) return null;
	return createPortal(children, el);
}

export default BalloonModal;
