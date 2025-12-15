import React from 'react';
import Layout from '@theme/Layout';
import Link from '@docusaurus/Link';

export default function Home(): JSX.Element {
  return (
    <Layout
      title="Physical AI & Humanoid Robotics"
      description="A textbook for learning Physical AI, Robotics, and Vision-Language-Action systems"
    >
      <main style={{ padding: '4rem 2rem', textAlign: 'center' }}>
        <h1>Physical AI & Humanoid Robotics</h1>
        <p style={{ maxWidth: '800px', margin: '1.5rem auto', fontSize: '1.1rem' }}>
          This textbook introduces the foundations of Physical AI and Humanoid Robotics,
          covering perception, planning, vision-language-action models, and autonomous humanoid systems.
          It is designed for students and developers preparing for the future of intelligent robotics.
        </p>

        <Link
          className="button button--primary button--lg"
          to="/docs/intro"
        >
          📘 Start Reading the Book
        </Link>
      </main>
    </Layout>
  );
}
