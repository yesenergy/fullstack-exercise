import React, { useEffect, useState } from 'react';
import './App.css';
import Card from '@material-ui/core/Card';
import CardActions from '@material-ui/core/CardActions';
import CardContent from '@material-ui/core/CardContent';
import { multiSort } from './util/SortUtil';
import { Row, Header } from './Row';
import { SummaryRow, SummaryHeader } from './SummaryRow';
import { ControlBar } from './ControlBar';
import { Spinner } from './Spinner';

const PAGESIZE = 20;

const List = ({ data }) => data.map((item, index) => <Row item={item} />);
const SummaryList = ({ data }) => data.map((item, index) => <SummaryRow item={item} />);

function App() {
	const [data, setData] = useState([]);
	const [summary, setSummary] = useState([]);
	const [loading, setLoading] = useState(false);
	const [loadingSummary, setLoadingSummary] = useState(false);
	const [page, setPage] = useState(1);
	const [sort, setSort] = useState('contractsize,participantfullname');
	const sortFunc = multiSort(sort.split(','));
	const pageData = data.sort(sortFunc).slice((page - 1) * PAGESIZE, page * PAGESIZE);
	useEffect(() => {
		async function fetchData() {
			setLoading(true);
			const trans = await fetch('/api/transactions');
			const json = await trans.json();
			setData(json);
			setLoading(false);
		}
		async function fetchSummary() {
			setLoadingSummary(true);
			const trans = await fetch('/api/summary');
			const json = await trans.json();
			setSummary(json);
			setLoadingSummary(false);
		}
		fetchData();
		fetchSummary();
	}, []);
	return (
		<>
			<Card id="summary">
				<CardActions id="summarytable">
					<CardContent>
						<>
							<SummaryHeader />
							<SummaryList data={summary} />
						</>
						</CardContent>
					</CardActions>
			</Card>
			<Card id="table">
				<CardActions id="controls">
					<ControlBar
						page={page}
						pages={Math.ceil(data.length / PAGESIZE)}
						setPage={setPage}
						sort={sort}
						setSort={setSort}
					/>
				</CardActions>
				<CardContent>
					<>
						<Header />
						<List data={pageData} />
					</>
				</CardContent>
			</Card>
			<Spinner spinning={loading||loadingSummary} />
		</>
	);
}

export default App;
