import SubmitProgram from './components/submitprogram/SubmitProgram';
import Banner from './components/banner/Banner';
import ProgramSummary from './components/programsummary/ProgramSummary';

function App() {
  return (
    <div className="App">
      <Banner></Banner>
      <SubmitProgram></SubmitProgram>
      <ProgramSummary></ProgramSummary>
    </div>
  );
}

export default App;
