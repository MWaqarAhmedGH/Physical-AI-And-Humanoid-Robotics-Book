import type {SidebarsConfig} from '@docusaurus/plugin-content-docs';

const sidebars: SidebarsConfig = {
  tutorialSidebar: [
    'intro',
    {
      type: 'category',
      label: 'Module 1: ROS 2 Nervous System',
      items: [
        'module-1-ros2/introduction',
        'module-1-ros2/quickstart',
        'module-1-ros2/exercises',
      ],
    },
    {
      type: 'category',
      label: 'Module 2: Digital Twin',
      items: [
        'module-2-digital-twin/introduction',
        'module-2-digital-twin/quickstart',
        'module-2-digital-twin/exercises',
      ],
    },
    {
      type: 'category',
      label: 'Module 3: NVIDIA Isaac',
      items: [
        'module-3-isaac/introduction',
        'module-3-isaac/quickstart',
        'module-3-isaac/exercises',
      ],
    },
    {
      type: 'category',
      label: 'Module 4: VLA',
      items: [
        'module-4-vla/introduction',
        'module-4-vla/quickstart',
        'module-4-vla/exercises',
      ],
    },
  ],
};

export default sidebars;