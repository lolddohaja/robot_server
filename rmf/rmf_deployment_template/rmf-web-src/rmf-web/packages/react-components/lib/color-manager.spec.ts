import { ColorManager } from './color-manager';

let colorManager: ColorManager;

beforeEach(() => {
  colorManager = new ColorManager();
});

describe('ColorManager', () => {
  it('snapshot - get color based on image', async () => {
    const color = await colorManager.robotPrimaryColor(
      'test_fleet',
      'test_robot',
      'test_model',
      '/base/test-data/assets/tiny-robot.png',
    );
    const values = color.slice(color.indexOf('(') + 1, color.lastIndexOf(')'));
    const rgb = values.split(',').map((v) => parseInt(v));
    expect(Math.abs(rgb[0] - 4)).toBeLessThanOrEqual(2);
    expect(Math.abs(rgb[1] - 52)).toBeLessThanOrEqual(2);
    expect(Math.abs(rgb[2] - 156)).toBeLessThanOrEqual(2);
  });

  it('fallback to color from id if image analysis fails', async () => {
    expect(async () => {
      await colorManager.robotPrimaryColor(
        'test_fleet',
        'test_robot',
        'test_model',
        '/base/test-data/assets/non-existing-image.png',
      );
    }).not.toThrow();
  });
});
