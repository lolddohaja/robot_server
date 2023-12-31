import { Meta, Story } from '@storybook/react';
import React from 'react';
import { AdminDrawer } from '../../components/admin/drawer';

export default {
  title: 'Admin/Drawer',
  component: AdminDrawer,
  argTypes: {
    active: {
      defaultValue: 'Users',
    },
  },
} as Meta;

export const Default: Story<{}> = (args) => {
  return <AdminDrawer {...args} />;
};

Default.storyName = 'Drawer';
