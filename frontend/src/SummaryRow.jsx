import React from 'react';
import { formatCurrency } from './util/FormatUtil.js';

export const SummaryRow = ({ item }) => (
	<div className="row">
		<div id="tradetype" className="column">
			{item.tradetype}
		</div>
		<div id="peaktype" className="column">
			{item.peaktype}
		</div>
		<div id="hedgetype" className="column">
			{item.hedgetype}
		</div>
		<div id="profit" className="column">
			{formatCurrency(item.profit)}
		</div>
	</div>
);

export const SummaryHeader = ({ item }) => (
	<div className="row header">
		<div id="tradetype" className="column">
			Trade Type
		</div>
		<div id="peaktype" className="column">
			Peak Type
		</div>
		<div id="hedgetype" className="column">
			Hedge Type
		</div>
		<div id="profit" className="column">
			Profit
		</div>
	</div>
);
