# IBM Quantum Awards: Open Science Prize 2022

IBM Quantum is excited to announce the fifth annual quantum awards (and the third annual Open Science Prize)—an award for the best open source solution to some of the most pressing problems in the field of quantum computing. 

This year, the challenge will feature one problem from the field of quantum ground state preparation. The best open source solution will receive a \$30,000 prize. The runner up will receive \$20,000. 

Preparing quantum states lies at the heart of quantum computing, and is essential to promising applications of near-term quantum processors. This year's problem asks participants to prepare the ground state of a Heisenberg spin-1/2 Hamiltonian on a kagome lattice using IBM Quantum's 16-qubit ibmq_guadalupe system. The ground states of such systems are highly entangled and linked to exotic quantum behavior at the forefront of quantum research. The goal is to compute the ground state energy with the highest fidelity using VQE. Note that this is the largest qubit system offered in an Open Science Prize to date. We look forward to another year of incredible solutions.

**Read more on the [blog](https://research.ibm.com/blog/ibm-quantum-open-science-prize-2022) post and register [here](https://ibmquantumawards.bemyapp.com/#/event)**.

The competition will conclude on April 15, 2023. 

*Once you register, we encourage you to join us on the Qiskit Slack Channel [#open-science-prize-22](https://qiskit.slack.com/archives/C04BF2X563C) to chat and ask questions. Join the Qiskit Slack workspace [here](https://ibm.co/joinqiskitslack), if you haven't already.*

Participants may submit their answer as outlined below:

- Each team or participant may only contribute to one submission
- Solution may only be executed on the designated device (ibmq_guadalupe)
- Each submission must use the VQE algorithm to optimize and measure the ground state energy under the specified Hamiltonian and lattice as outlined in the included Jupyter Notebook.
- Only use libraries that can be installed using either pip install or conda install, and no purchased libraries.
- Document code with concise, clear language about the chosen methodology.
- The relative error of the measured ground state energy must be below 1% for consideration.

The submissions will be judged on the following criteria:

- Performance as measured by the relative error of the measured ground state energy w.r.t. the exact value in comparison to other submissions (Max 25 points).
- Scalability of the solution to larger qubit devices and larger kagome lattices (Max 5 points)
- Creativity in developing a unique, innovative, and original solution (Max 5 points)
- Clarity of provided documentation and solution code (Max 5 points)

# Open Science
The goal of the Prize is to make significant progress on challenges at the forefront of quantum computation by doing science in the open. The resulting solutions will be open-sourced for the benefit of the entire quantum computing community.
